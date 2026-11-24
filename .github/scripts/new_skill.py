#!/usr/bin/env python3
"""Scaffold a skill, and its plugin if the plugin is new.

Usage (through pixi):
    pixi run new-skill <plugin> <skill> --maintainer @handle [--core] [--agent NAME]
    pixi run scaffold-check          # CI gate: no TODO(scaffold) placeholder left

What it writes:

- a new plugin (only if ``<plugin>`` doesn't exist yet) under
  ``community-plugins/<plugin>/`` (or ``plugins/<plugin>/`` with ``--core``):
  ``plugin.json``, ``README.md``, a copy of the root ``LICENSE``, a
  ``.claude-plugin/marketplace.json`` entry and a ``docs/catalog.yml`` entry;
- ``skills/<skill>/SKILL.md`` from the template below;
- with ``--agent NAME``, ``agents/NAME.md`` that preloads the new skill;
- an ``example:`` line for the skill in ``docs/catalog.yml``.

Then it runs ``agent_plugins.py sync`` and ``skill_catalog.py sync`` so every
generated file is current. Each placeholder it leaves is marked
``TODO(scaffold)``; ``--check`` fails while any remain, so a half-filled
template cannot merge.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = Path(__file__).resolve().parent
MARK = "TODO(scaffold)"
NAME = re.compile(r"^(?!.*--)[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
HANDLE = re.compile(r"^@[A-Za-z0-9-]+(?:/[A-Za-z0-9._-]+)?$")
REPO_URL = "https://github.com/gaia-hazlab/gaia-skills"

SKILL_TEMPLATE = """\
---
name: {skill}
description: >-
  {mark} One sentence on what this skill does, naming the data, code or method
  it works with. Use when the user asks to "phrase one", "phrase two" or
  "phrase three", or mentions <tool, dataset, region>. Keep the whole text
  between 100 and 1024 characters; it is all the agent reads when deciding to
  load the skill.
---

# {title}

{mark} Write this body for an agent that is fluent in Python and geoscience
but has never seen your workflow. Keep it under ~500 lines; move long material
into `references/` inside this skill directory and link to it.

## When to use

- {mark} The situations this skill covers, and the ones it does not.

## Workflow

1. {mark} The steps in the order you would do them, with the exact commands.
2. Say what to check after each step and what a wrong result looks like.

## Conventions

- {mark} Units, coordinate reference systems, file formats, naming, data
  sources and their licences: whatever a newcomer would get wrong.

## Verification

- {mark} How the agent proves the result is right before reporting it
  (a test, a known value, a plot to inspect).
"""

AGENT_TEMPLATE = """\
---
name: {agent}
description: >-
  {mark} Use this agent when the user needs <task>. Say what it produces and
  when the main conversation should hand work to it rather than do it inline.
model: inherit
skills:
  - {skill}
---

{mark} You are a specialist in <domain> for GAIA HazLab. State the goal, the
inputs you expect, what you return, and what you must never do without asking
the user (download large data, write outside the project, spend money).
"""

README_TEMPLATE = """\
# {plugin}

{mark} One paragraph: what this plugin helps an agent do, for which part of
GAIA, and who maintains it ({maintainer}).

## Skills

| Skill | What it does |
| --- | --- |
| `{skill}` | {mark} |

## What it may run

{mark} List every command or script the skills tell the agent to run, and
what each needs network access for. Reviewers check this against the
security checklist in CONTRIBUTING.md.

## Install

```bash
claude plugin marketplace add gaia-hazlab/gaia-skills
claude plugin install {plugin}@gaia-skills
```
"""


def fail(msg: str) -> None:
    sys.exit(f"new-skill: {msg}")


def write_new(path: Path, text: str, root: Path) -> None:
    if path.exists():
        fail(f"{path.relative_to(root)} already exists; not overwriting it")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"  wrote {path.relative_to(root)}")


def find_plugin(root: Path, plugin: str) -> Path | None:
    for parent in ("plugins", "community-plugins"):
        if (root / parent / plugin).is_dir():
            return root / parent / plugin
    return None


def add_marketplace_entry(root: Path, plugin: str, rel: str, category: str) -> None:
    path = root / ".claude-plugin/marketplace.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["plugins"].append({"name": plugin, "source": f"./{rel}", "category": category, "strict": False})
    path.write_text(json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  added {plugin} to .claude-plugin/marketplace.json")


def add_catalog_plugin(root: Path, plugin: str, tier: str, maintainer: str, skill: str) -> None:
    path = root / "docs/catalog.yml"
    text = path.read_text(encoding="utf-8").rstrip("\n")
    text += (f"\n\n  {plugin}:\n    tier: {tier}\n    maintainer: \"{maintainer}\"\n    skills:\n"
             f"      {skill}:\n        example: {MARK} a request a user would type that should load this skill.\n")
    path.write_text(text, encoding="utf-8")
    print(f"  added {plugin} to docs/catalog.yml")


def add_catalog_skill(root: Path, plugin: str, skill: str) -> None:
    """Insert the skill under an existing plugin's `skills:` key, keeping the file's comments."""
    path = root / "docs/catalog.yml"
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    try:
        start = next(i for i, ln in enumerate(lines) if ln.rstrip() == f"  {plugin}:")
        at = next(i for i in range(start + 1, len(lines)) if lines[i].rstrip() == "    skills:")
    except StopIteration:
        fail(f"docs/catalog.yml has no `skills:` block under `{plugin}:`; add the skill there by hand")
    lines.insert(at + 1, f"      {skill}:\n        example: {MARK} a request a user would type that should load this skill.\n")
    path.write_text("".join(lines), encoding="utf-8")
    print(f"  added {plugin}/{skill} to docs/catalog.yml")


def scaffold(root: Path, plugin: str, skill: str, maintainer: str, core: bool, agent: str | None,
             run_sync: bool = True) -> None:
    for label, value in (("plugin", plugin), ("skill", skill), ("agent", agent)):
        if value is not None and not NAME.match(value):
            fail(f"{label} name {value!r} must be lowercase letters, digits and single hyphens")
    pdir = find_plugin(root, plugin)
    if pdir is None:
        if not maintainer or not HANDLE.match(maintainer):
            fail("a new plugin needs --maintainer @github-handle (or @org/team)")
        rel = f"{'plugins' if core else 'community-plugins'}/{plugin}"
        pdir = root / rel
        manifest = {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "name": plugin,
            "version": "0.1.0",
            "description": f"{MARK} one line on what this plugin does",
            "author": {"name": "GAIA HazLab", "url": "https://github.com/gaia-hazlab"},
            "repository": REPO_URL,
            "license": "MIT",
            "keywords": ["gaia", "geohazards"],
        }
        print(f"New plugin {rel}:")
        write_new(pdir / "plugin.json", json.dumps(manifest, indent=4) + "\n", root)
        write_new(pdir / "README.md", README_TEMPLATE.format(plugin=plugin, skill=skill, maintainer=maintainer, mark=MARK), root)
        shutil.copyfile(root / "LICENSE", pdir / "LICENSE")
        print(f"  wrote {rel}/LICENSE (copy of the root MIT license)")
        add_marketplace_entry(root, plugin, rel, "core" if core else "community")
        add_catalog_plugin(root, plugin, "Core" if core else "Community", maintainer, skill)
    else:
        if (pdir / "skills" / skill).exists():
            fail(f"{(pdir / 'skills' / skill).relative_to(root)} already exists; not overwriting it")
        if agent and (pdir / "agents" / f"{agent}.md").exists():
            fail(f"{(pdir / 'agents' / agent).relative_to(root)}.md already exists; not overwriting it")
        print(f"Existing plugin {pdir.relative_to(root)}:")
        add_catalog_skill(root, plugin, skill)
    title = skill.replace("-", " ").capitalize()
    write_new(pdir / "skills" / skill / "SKILL.md", SKILL_TEMPLATE.format(skill=skill, title=title, mark=MARK), root)
    if agent:
        write_new(pdir / "agents" / f"{agent}.md", AGENT_TEMPLATE.format(agent=agent, skill=skill, mark=MARK), root)
    if run_sync:
        for script in ("agent_plugins.py", "skill_catalog.py"):
            subprocess.run([sys.executable, str(SCRIPTS / script), "sync", "--root", str(root)], check=True)
    print(f"\nNext: replace every {MARK} marker, then run `pixi run check-all`.")


def leftovers(root: Path) -> list[str]:
    hits = []
    targets = [root / "docs/catalog.yml"]
    for parent in ("plugins", "community-plugins"):
        if (root / parent).is_dir():
            targets += sorted(p for p in (root / parent).rglob("*") if p.is_file())
    for path in targets:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if MARK in line:
                hits.append(f"{path.relative_to(root)}:{n}: {line.strip()}")
    return hits


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("plugin", nargs="?")
    ap.add_argument("skill", nargs="?")
    ap.add_argument("--maintainer", help="GitHub handle that owns a new plugin, e.g. @your-handle")
    ap.add_argument("--core", action="store_true", help="put a new plugin under plugins/ (Core tier)")
    ap.add_argument("--agent", help="also create agents/<AGENT>.md that preloads the skill")
    ap.add_argument("--check", action="store_true", help="fail if any TODO(scaffold) placeholder remains")
    ap.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    ap.add_argument("--no-sync", action="store_true", help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    root = args.root.resolve()
    if args.check:
        hits = leftovers(root)
        for h in hits:
            print(h)
        if hits:
            print(f"\n{len(hits)} scaffold placeholder(s) left; replace each {MARK} before merging.")
        return 1 if hits else 0
    if not (args.plugin and args.skill):
        ap.error("give a plugin and a skill name, or --check")
    scaffold(root, args.plugin, args.skill, args.maintainer or "", args.core, args.agent, not args.no_sync)
    return 0


if __name__ == "__main__":
    sys.exit(main())
