# Contributor guide

This guide is for GAIA group members and collaborators who want to add to gaia-skills: a skill,
an agent, a command, or a fix to someone else's. It goes from setting up your machine to
maintaining your plugin after it merges.

The rules the checks enforce and the security review checklist are in
[CONTRIBUTING.md](../CONTRIBUTING.md). Agents have their own walkthrough in
[adding-an-agent.md](adding-an-agent.md).

## What you can contribute

| Contribution | Where it goes | Start with |
| --- | --- | --- |
| A skill: the method for one task, written for an agent | `<plugin>/skills/<skill>/SKILL.md` | [Add a skill](#add-a-skill) |
| An agent: a subagent that does a whole job and reports back | `<plugin>/agents/<agent>.md` | [adding-an-agent.md](adding-an-agent.md) |
| A command: a `/slash-command` for a prompt you run often | `<plugin>/commands/<command>.md` | [Add a command](#add-a-command) |
| Reference material or a helper script for a skill | `<skill>/references/`, `<skill>/scripts/` | [References and scripts](#references-and-scripts) |
| A fix to a plugin you don't maintain | that plugin | [Change an existing plugin](#change-an-existing-plugin) |
| An idea you won't write yourself | an issue | the **New skill or agent idea** issue template |

Good first contributions are workflows you already explain to new students: how to stage a
dataset, which quality checks to run on a product, how to set up a model run, which station or
product to trust and why.

## One-time setup

1. **GitHub access.** Members of the `gaia-hazlab` organization push branches to this
   repository. Collaborators outside the organization fork it and open pull requests from the
   fork; everything else in this guide is the same.
2. **Tools.** Install [git](https://git-scm.com/), the [GitHub CLI](https://cli.github.com/)
   (`gh`), [pixi](https://pixi.sh) and [Claude Code](https://docs.claude.com/en/docs/claude-code).
3. **Clone and install the tooling:**

   ```bash
   git clone https://github.com/gaia-hazlab/gaia-skills.git
   cd gaia-skills
   pixi install -e ci
   pixi run check-all      # should pass on a fresh clone
   ```

4. **Install the helper plugin** so Claude Code can coach you while you write:

   ```bash
   claude plugin marketplace add gaia-hazlab/gaia-skills
   claude plugin install gaia-core@gaia-skills
   ```

   It gives you the `authoring-gaia-skills` skill and the `skill-reviewer` agent.

## Before you write

- **Look for an existing home.** Read the [skill catalog](catalog.md). If a plugin already
  covers your domain, add your skill to it and tell its maintainer. Otherwise create your own
  plugin under `community-plugins/`.
- **Claim the work.** Open an issue with the **New skill or agent idea** template and assign
  yourself, so two people don't write the same skill.
- **Gather your source material**: the notebook, script, README or notes the skill will be
  based on, and three or four requests a colleague would type when they need it.
- **Name things by the task.** Plugins are named for a domain (`gaia-seismic-landslides`,
  `gaia-insar`), skills for a task (`picking-landslide-signals`, `staging-insar-stacks`).
  Lowercase, single hyphens, no personal or project names.
- **Core or Community?** Your own domain plugin is Community and you maintain it. Core
  (`plugins/`) is for cross-cutting GAIA tooling maintained by the leads; ask them before
  adding there.

## Add a skill

1. **Branch:**

   ```bash
   git switch main && git pull
   git switch -c add-<skill>
   ```

2. **Scaffold.** This creates the plugin too if it doesn't exist, with you as maintainer:

   ```bash
   pixi run new-skill <plugin> <skill> --maintainer @your-github-handle
   # --agent <name>  also create an agent that preloads the skill
   ```

   It writes `plugin.json`, `README.md`, `LICENSE` and `skills/<skill>/SKILL.md`, and registers
   the plugin in `.claude-plugin/marketplace.json` and `docs/catalog.yml`.

3. **Write.** Replace every `TODO(scaffold)` placeholder; `pixi run scaffold-check` lists them.
   In Claude Code, with `gaia-core` installed, you can say *"help me turn my notebook into a
   gaia skill"* and point it at your source material.
   - **The description** decides whether the skill ever loads. 100 to 1024 characters: what it
     does, naming the data or tool, then `Use when the user asks to "...", "..." or "...".`
   - **The body** is for an agent that knows Python and geoscience but not your workflow. Steps
     in order with exact commands, conventions (units, CRS, time zones, data quirks), and how
     to verify the result. Keep it under about 500 lines.
   - **The catalog example** in `docs/catalog.yml`: a self-contained request a colleague would
     type.
   - **The plugin README**: what the plugin does and every command or script it may run.

4. **Check and try it:**

   ```bash
   pixi run sync
   pixi run check-all
   claude --plugin-dir community-plugins/<plugin>
   ```

   In that session type your catalog example. If the skill doesn't load, rewrite the
   description, not the example.

5. **Open the pull request** (see [Pull request and review](#pull-request-and-review)).

## Add an agent

Follow [adding-an-agent.md](adding-an-agent.md). In short: put the method in a skill, then add
an agent that preloads it with `pixi run new-skill <plugin> <skill> --agent <agent> ...`, or
write `agents/<agent>.md` by hand for an existing skill.

## Add a command

Claude Code now recommends skills over commands for new work. A plugin skill can also be run
by typing `/<plugin>:<skill>`, and skills work in other assistants while commands don't. So
write a skill unless you want a fixed prompt that only makes sense when a person types it.

A command is a Markdown file you create by hand at `<plugin>/commands/<command>.md`:

```markdown
---
description: Summarise what GAIA data exist for a region and time window
argument-hint: <region> <start-year> <end-year>
---

List the GAIA datasets that cover $0 between $1 and $2, using the
staging conventions from the gaia-data-staging skill. ...
```

- `$ARGUMENTS` is everything the user typed after the command; `$0`, `$1`, ... are the
  individual arguments, counting from zero.
- Other supported fields include `allowed-tools` and `model`. Pre-approving tools with
  `allowed-tools` skips the user's permission prompts for them, so explain any use of it in the
  pull request.
- Users run it as `/<plugin>:<command>`. Test it with `claude --plugin-dir <plugin-dir>` and
  type `/` to find it.

## References and scripts

- **References.** Long tables, data-source notes, parameter lists and code templates go in
  `skills/<skill>/references/<topic>.md`. Link each one from `SKILL.md` and say when to read
  it, e.g. *"For CONUS404 variable names, read `[references/conus404.md](references/conus404.md)`."*
- **Scripts.** Helper scripts go in `skills/<skill>/scripts/`. They must be executable
  (`chmod +x`), read and write only paths the user gives them, and use the network only for the
  data source the user asked for. Document each one in the plugin README.
- **Stay inside the skill folder.** Clients install one skill folder at a time, so a link to
  `../other-skill/` or the repository root breaks after install. `pixi run check-all` catches
  this.
- **No data files.** Don't commit datasets, model output or large binaries. Point to where the
  data lives and how to fetch it.

## MCP servers

A plugin can ship an MCP server that gives agents new tools (for example a catalog search
service). That brings code and possibly credentials into every user's session, so talk to the
GAIA leads before adding one. A plugin with a server needs both `.mcp.json` (Claude Code) and
`mcp.json` (other clients); see the rules in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Change an existing plugin

- **Your own plugin:** change it, bump `version` in its `plugin.json` (patch for fixes, minor
  for a new skill or agent, major if a user's existing request would stop working), run
  `pixi run sync`, and add a line to [CHANGELOG.md](../CHANGELOG.md) under the plugin's name.
- **Always bump the version.** Claude Code updates an installed plugin only when its
  `version` changes. Merge a change without bumping it and nobody who already installed the
  plugin gets it.
- **Someone else's plugin:** open an issue or a pull request and mention the maintainer named in
  [catalog.md](catalog.md). Don't rewrite their skill wholesale; fix the specific problem.
- **Renaming or removing** a skill, agent or command breaks users who rely on it. Announce it in
  an issue first, say what replaces it, and mention it in the GAIA channel.

## Pull request and review

```bash
git add -A
git commit -m "Add <skill> skill to <plugin>"
git push -u origin HEAD
gh pr create
```

Fill in the template: what changed, what the skills may run, how you tested, and which parts an
AI assistant wrote. Then:

1. **CI runs automatically.** *Validate Plugins* runs the same checks as `pixi run check-all`,
   validates the manifests against the Agent Plugins schemas, runs
   `claude plugin validate --strict`, and scans for secrets and dangerous command patterns.
   *Test CI scripts* runs when the tooling changes. A failed check shows its log on the pull
   request.
2. **Copilot posts an automated review** on every pull request. Treat its comments as
   suggestions: fix the ones that are right, reply to the ones that aren't, and resolve the
   threads.
3. **Run the reviewer agent yourself** before asking for a human review:

   ```text
   Use the skill-reviewer agent to review community-plugins/<plugin>
   ```

4. **A maintainer reviews** against the security checklist in
   [CONTRIBUTING.md](../CONTRIBUTING.md) and merges. Expect questions about every command, URL
   and tool permission in your plugin.

Using an AI assistant to write a skill is expected. You still own every line: read the whole
diff, run the checks yourself, and be ready to explain any instruction in it.

## After it merges

Users get your change when they next run `claude plugin update` (see the
[user guide](user-guide.md#update-disable-or-remove)), and only if you bumped `version`. Post the catalog example in the GAIA
channel so people know to try it.

## Maintaining your plugin

As maintainer you are the person issues about your plugin are routed to.

- Watch the repository (or at least issues that mention you) and answer reports about your
  skills.
- When a package, endpoint or data product your skill names changes, update the skill and bump
  the version.
- If you leave the group or stop maintaining it, change `maintainer` in `docs/catalog.yml` to
  the person taking over, or open an issue asking the leads to find someone.

## Quick reference

| Task | Command |
| --- | --- |
| Install tooling | `pixi install -e ci` |
| New skill (and plugin) | `pixi run new-skill <plugin> <skill> --maintainer @you` |
| New skill with an agent | add `--agent <agent>` |
| List unfilled placeholders | `pixi run scaffold-check` |
| Regenerate manifests and catalog | `pixi run sync` |
| Run every CI check | `pixi run check-all` |
| Also run Claude's validator | `pixi run plugins-check-claude` |
| Try a plugin locally | `claude --plugin-dir <plugin-dir>` |
