---
name: authoring-gaia-skills
description: >-
  Turns a GAIA researcher's workflow (a notebook, script, processing recipe or
  data-access routine) into an agent skill or subagent in the gaia-skills
  repository, with frontmatter, catalog entry and checks that pass CI. Use when
  the user asks to "write a skill", "turn this notebook into a skill", "add my
  workflow to gaia-skills", "make a Claude skill", "create a subagent", or to
  fix a SKILL.md description that doesn't trigger.
---

# Authoring GAIA skills

A skill is a folder with a `SKILL.md`: a description the agent reads to decide whether to
load it, and a body it reads once loaded. Good GAIA skills encode what a new student gets
wrong: units, coordinate reference systems, data quirks, which station or product to trust,
which check proves the result.

## 1. Interview before writing

Ask the user, one or two questions at a time, until you can answer all of these:

1. What task does the skill cover, and what does it produce (a script, a dataset, a figure, a
   decision)? What is out of scope?
2. What would a user type when they need it? Collect three or four real phrasings.
3. Which code, packages, data sources and services does it use? Pinned versions, endpoints,
   credentials needed (never the credentials themselves).
4. What does a correct result look like, and how does one check it (a known event, a
   reference value, a plot)?
5. What do newcomers get wrong?

Read the user's source material (notebook, script, README) before drafting. Do not invent
endpoints, parameters or package APIs: if the source doesn't show it, ask.

## 2. Scaffold

From the root of a gaia-skills checkout:

```bash
pixi run new-skill <plugin> <skill> --maintainer @their-github-handle
# add --agent <agent-name> to also create a subagent that preloads the skill
# add --core only for cross-cutting GAIA tooling the leads will maintain
```

Use an existing plugin when the skill fits one (check `docs/catalog.md`). Names are lowercase
with single hyphens; prefer a gerund or noun phrase that says the task (`picking-landslide-signals`,
`staging-insar-stacks`), not the person or project.

## 3. Replace every placeholder the scaffold left

`pixi run scaffold-check` lists them with file and line.

Write the description first; it decides whether the skill ever loads.

- 100 to 1024 characters, third person. First what it does, naming the data or tool. Then
  `Use when the user asks to "...", "..." or mentions <tool, dataset, region>.`
- Quote the real phrasings from the interview. Name specific products and codes (HyP3,
  NoisePy, MODFLOW 6, CONUS404) since those are what users type.

Then the body:

- Steps in the order the user does them, with exact commands, and the check after each step.
- Conventions as short bullets. Numbers with units and their source.
- Keep it under about 500 lines. Long tables, API notes and templates go in
  `references/<topic>.md` inside the same skill folder, linked from the body.
- Every file and link must stay inside the skill's own folder; skills install one folder at a
  time. Name a sibling skill in prose instead of linking to it.
- Bundled scripts go in `scripts/`, must be executable, and must read and write only paths the
  user gives them.

Then the catalog: replace the `example:` placeholder in `docs/catalog.yml` with a
self-contained request a user would type (no references to files that don't exist).

For an agent file, see [references/agents.md](references/agents.md).

## 4. Check and try it

```bash
pixi run sync        # regenerate manifests and docs/catalog.md
pixi run check-all   # the same gates CI runs
claude --plugin-dir <plugin-dir>   # then type the catalog example and confirm the skill loads
```

If the skill does not load on the example, change the description, not the example.

## 5. Open the pull request

Fill in the pull request template, including what the skills may run. Ask a reviewer to run the
`skill-reviewer` agent on the plugin directory, or run it yourself first.
