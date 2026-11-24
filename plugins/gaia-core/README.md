# gaia-core

Helps a GAIA group member turn a research workflow into an agent skill or subagent in this
repository, and helps a reviewer check one before it merges. Maintained by @mdenolle.

## Contents

| Kind | Name | What it does |
| --- | --- | --- |
| Skill | `authoring-gaia-skills` | Interviews you about a workflow and drafts a `SKILL.md` that passes this repository's checks |
| Agent | `skill-reviewer` | Reads one plugin directory and reports problems against the security checklist and the authoring rules |

## What it may run

- `pixi run new-skill`, `pixi run sync` and `pixi run check-all` inside a gaia-skills checkout.
  These read and write files in that checkout only and need no network access after `pixi install`.
- `rg` (ripgrep) searches over a plugin directory, read-only.
- `claude --plugin-dir <dir>` to try a skill locally.

Nothing in this plugin downloads data, calls an external API or writes outside the repository.

## Install

```bash
claude plugin marketplace add gaia-hazlab/gaia-skills
claude plugin install gaia-core@gaia-skills
```
