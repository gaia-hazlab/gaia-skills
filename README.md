# gaia-skills

[![Validate Plugins](https://github.com/gaia-hazlab/gaia-skills/actions/workflows/validate-plugins.yml/badge.svg?branch=main)](https://github.com/gaia-hazlab/gaia-skills/actions/workflows/validate-plugins.yml?query=branch%3Amain)
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)

Agent plugins for GAIA HazLab. Each plugin bundles **skills** (instructions an AI coding agent
loads when a request matches them), and may add **subagents** and **commands** for Claude Code.
The aim is that the know-how each group member holds about their data, codes and methods
(seismology, hydrology, geodesy, SAR, landslides, debris flows, data staging) becomes something
an agent can pick up and use correctly.

The layout and tooling follow [uw-ssec/savvy](https://github.com/uw-ssec/savvy), the UW
Scientific Software Engineering Center's plugin collection. Plugins use the
[Agent Plugins](https://agent-plugins.org/specification) format, so the skills also work in
GitHub Copilot, Codex, Cursor and OpenCode.

## Install

In Claude Code:

```bash
claude plugin marketplace add gaia-hazlab/gaia-skills
claude plugin install gaia-core@gaia-skills
```

Other clients: follow savvy's [installation guide](https://github.com/uw-ssec/savvy/blob/main/docs/install.md)
with `gaia-hazlab/gaia-skills` in place of `uw-ssec/savvy`.

> [!IMPORTANT]
> Skills are instructions, not programs, but your agent acts on them: it may run commands, edit
> files and use the network within the permissions your client allows. Every plugin README lists
> what its skills may run. Read it before installing.

## What's here

The [skill catalog](docs/catalog.md) lists every plugin, skill, agent and command, with trigger
phrases, an example prompt and the maintainer.

| Directory | Tier | What goes there |
| --- | --- | --- |
| [plugins/](plugins/) | Core | Cross-cutting GAIA tooling, maintained by the GAIA leads |
| [community-plugins/](community-plugins/) | Community | Each group member's own plugins for their domain |

## Add your own skill

```bash
pixi install -e ci
pixi run new-skill <plugin> <skill> --maintainer @your-github-handle
```

Then follow [CONTRIBUTING.md](CONTRIBUTING.md). To add an agent (a Claude Code subagent), follow
[docs/adding-an-agent.md](docs/adding-an-agent.md). With the `gaia-core` plugin installed you can also
ask Claude Code "help me turn my notebook into a gaia skill" and it will walk you through it.

## Related repositories

- [gaia-agentic-ai](https://github.com/gaia-hazlab/gaia-agentic-ai): the GAIA agent project,
  golden tasks and evaluation design. Skills built here are what those agents run on.
- [uw-ssec/savvy](https://github.com/uw-ssec/savvy): general research-software plugins (pixi,
  testing, packaging, containers, Zarr). Install it alongside this marketplace rather than
  copying its skills here.

## License

MIT, see [LICENSE](LICENSE). A plugin may bundle a different license in its own `LICENSE` file
(for example `gaia-data-downloader` is BSD-3-Clause). The repository tooling in
`.github/scripts/` is adapted from savvy under BSD-3-Clause, see
[.github/scripts/LICENSE-savvy](.github/scripts/LICENSE-savvy).
