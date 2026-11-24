# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Cursor, Copilot and others) working on this
repository. This file guides work *on* gaia-skills; it is not part of any plugin.

## What this repository is

A marketplace of agent plugins for GAIA HazLab, laid out like
[uw-ssec/savvy](https://github.com/uw-ssec/savvy). Plugins live in `plugins/` (Core tier) and
`community-plugins/` (Community tier). Each has a source `plugin.json`, a README, a LICENSE and
some of `skills/`, `agents/`, `commands/`.

## Non-negotiables

1. **Pixi only.** Run tooling with `pixi run <task>` (environment `ci`). Never call `pip`,
   `conda` or `venv`.
2. **Verify before you claim.** Don't report work as done until `pixi run check-all` passes and
   you have read its output.
3. **Never hand-edit generated files**: `<plugin>/.claude-plugin/plugin.json`,
   `.agents/plugins/marketplace.json`, `.cursor-plugin/marketplace.json`, `docs/catalog.md`.
   Edit the sources and run `pixi run sync`.
4. **Change surgically.** Touch only the plugin the request is about. Don't reformat or
   "improve" someone else's plugin; its README names the maintainer.
5. **Ask instead of assuming** about endpoints, parameters, package APIs or data conventions a
   skill should state. If the user's source material doesn't show it, ask.
6. **Security.** Every plugin change must pass the security review checklist in
   `CONTRIBUTING.md`. Never write credentials, tokens, private URLs or personal data into a
   plugin.

## Tasks

| Task | Command |
| --- | --- |
| Scaffold a skill (and plugin if new) | `pixi run new-skill <plugin> <skill> --maintainer @handle [--agent NAME] [--core]` |
| Regenerate manifests and catalog | `pixi run sync` |
| All offline CI gates | `pixi run check-all` |
| Also run `claude plugin validate --strict` | `pixi run plugins-check-claude` |
| Try a plugin locally | `claude --plugin-dir <plugin-dir>` |

## Where things are

| Path | Role |
| --- | --- |
| `.claude-plugin/marketplace.json` | Source: plugin list, `source`, `category`, `strict` |
| `docs/catalog.yml` | Source: tier, maintainer, example prompt per skill |
| `.github/scripts/agent_plugins.py` | Manifest sync and package checks (from savvy) |
| `.github/scripts/skill_catalog.py` | Generates `docs/catalog.md` (from savvy) |
| `.github/scripts/new_skill.py` | Scaffolder and `TODO(scaffold)` gate |
| `.github/workflows/validate-plugins.yml` | CI: checks, schemas, security scans |
