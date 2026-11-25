# User guide

This guide is for anyone who wants to use GAIA's skills and agents in their own research: install
them, use them, keep them up to date, and know what to watch for. You don't need to contribute
to use them. If you want to add your own, see the [contributor guide](contributor-guide.md).

## What you get

gaia-skills is a *marketplace*: a list of plugins your AI coding assistant can install. Each
plugin bundles some of:

| Part | What it does | How you use it |
| --- | --- | --- |
| **Skills** | Know-how for a task (staging a dataset, building a download script, writing a skill). The assistant loads one when your request matches it | Just ask for the task in plain words |
| **Agents** | A separate assistant that takes a whole job, works on it in its own context, and reports back | Ask for it by name: *"Use the data-downloader agent to ..."* |
| **Commands** | A `/slash-command` for a prompt you run often | Type `/` and pick it |

The [skill catalog](catalog.md) lists every plugin, what each skill does, the phrases that
trigger it, an example request to try, and who maintains it.

## Before you install

Skills are instructions, not programs, but your assistant acts on them. With a plugin installed
it may run commands, write files, download data and use the network, within the permissions you
give it. So:

- **Read the plugin's README** first. Each one lists what its skills may run and why they need
  the network.
- **Keep your permission prompts on.** Approve commands one at a time until you trust a
  workflow. No GAIA plugin should ask you to turn prompts off; if one does, report it.
- **Keep credentials in environment variables** (or your system keychain), never in a prompt or
  a file the assistant writes. Skills name the variable they expect.

## Install in Claude Code

From a terminal:

```bash
claude plugin marketplace add gaia-hazlab/gaia-skills
claude plugin install gaia-core@gaia-skills
claude plugin install gaia-data-downloader@gaia-skills
```

Or inside a Claude Code session: `/plugin marketplace add gaia-hazlab/gaia-skills`, then
`/plugin` to browse and install. The marketplace is named `gaia-skills`, which is why every
plugin ends in `@gaia-skills`. A new plugin loads in your next session, or run `/reload-plugins` in the current one.

Check what you have, and what one plugin contains:

```bash
claude plugin list
claude plugin details gaia-core@gaia-skills   # its skills, agents and token cost
```

Install only the plugins you need. Every installed skill and agent adds its description to
each session (`plugin details` shows the cost), and a dozen irrelevant ones make it harder for
the right skill to load.

## Set it up for a project or team

If a project repository should use GAIA plugins, record that in the repository so every
collaborator is pointed at them. From the project root:

```bash
claude plugin marketplace add gaia-hazlab/gaia-skills --scope project
claude plugin install gaia-data-downloader@gaia-skills --scope project
git add .claude/settings.json
git commit -m "Use GAIA plugins in this project"
```

This writes two entries to `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "gaia-skills": {
      "source": { "source": "github", "repo": "gaia-hazlab/gaia-skills" }
    }
  },
  "enabledPlugins": {
    "gaia-data-downloader@gaia-skills": true
  }
}
```

What a collaborator sees after cloning:

1. Claude Code asks them to **trust the folder**. Until they do, the marketplace entry is
   ignored.
2. The plugin is **not installed automatically**. The **Errors** tab in `/plugin` says it isn't
   installed here. Each person runs, once per clone:

   ```bash
   claude plugin install gaia-data-downloader@gaia-skills --scope project
   ```

   and then starts a new session or runs `/reload-plugins`.

Say this in the project's README so collaborators know to do it.

## Use it

**Skills load on their own.** Describe the task the way you would to a colleague, naming the
data, region and time window:

> Write a download script for CONUS404 daily precipitation over the Skagit watershed for
> water years 2015 to 2020, saved as Zarr.

If the assistant answers without using the skill (it tends to for short or vague requests),
name it: *"Use the download-script-dev skill to ..."*.

**Agents run when you ask for them.** For a small task the assistant usually does the work
itself; name the agent when you want it:

> Use the data-downloader agent to fetch HRRR 2 m temperature for January 2024 over
> western Washington.

GAIA agents propose a plan (sources, parameters, output location, expected download size) and
wait for your approval before doing anything large. Read the proposal; it is where wrong
assumptions get caught.

**See what's loaded** inside a session:

| Type | To see or do |
| --- | --- |
| `/plugin` | installed plugins and marketplaces, and an **Errors** tab; install, disable or remove |
| `/skills` | available skills. Plugin skills are named `<plugin>:<skill>` |
| `/reload-plugins` | load plugin changes without restarting |

Plugin agents are named `<plugin>:<agent>`, e.g. `gaia-core:skill-reviewer`. To list a
plugin's agents, run `claude plugin details <plugin>@gaia-skills` in a terminal.

## Working well with GAIA agents

- **Check the result, not just the summary.** Skills tell the assistant how to verify its work
  (a known event, a reference value, a plot). Ask to see that check.
- **Keep provenance.** Ask the assistant to record data sources, versions, parameters and
  commands in your project (a README or a config file), not only in the chat.
- **Watch costs.** Downloads, HPC jobs and cloud resources cost time, allocation or money.
  Agents should ask first; say no if the estimate looks wrong.
- **Mind data licences.** Some providers restrict redistribution. The skill should say so; if it
  doesn't and you're unsure, ask before publishing derived data.

## Update, disable or remove

Plugins improve as group members fix and extend them. To get the latest:

```bash
claude plugin marketplace update gaia-skills      # refresh the list of plugins and versions
claude plugin update gaia-core@gaia-skills         # update one installed plugin
```

The new version loads in your next session (or after `/reload-plugins`). Updating the
marketplace alone doesn't change installed plugins.

Automatic updates are off by default for this marketplace. To turn them on, open `/plugin`,
go to **Marketplaces**, and enable auto-update for `gaia-skills`.

To stop using a plugin without removing it: `claude plugin disable <plugin>@gaia-skills`
(`enable` turns it back on). To remove it: `claude plugin uninstall <plugin>@gaia-skills`. To
remove the whole marketplace: `claude plugin marketplace remove gaia-skills`.

## Other assistants

Skills follow the open [Agent Skills](https://agentskills.io/) format and work in other
assistants. Agents and commands are written for Claude Code.

| Assistant | Skills | Agents | Commands | Install |
| --- | --- | --- | --- | --- |
| Claude Code | yes | yes | yes | this guide |
| GitHub Copilot CLI | yes | no | no | `copilot plugin marketplace add gaia-hazlab/gaia-skills`, then `copilot plugin install <plugin>@gaia-skills` |
| Codex | yes | no | no | `codex plugin marketplace add gaia-hazlab/gaia-skills`, then `codex plugin add <plugin>@gaia-skills` |
| Cursor | yes | yes | yes | copy the plugin folder into `~/.cursor/plugins/local/` |
| VS Code, Antigravity CLI, OpenCode | yes | varies | varies | see savvy's guide |

These rows follow uw-ssec/savvy's [installation guide](https://github.com/uw-ssec/savvy/blob/main/docs/install.md),
which this repository mirrors; use it with `gaia-hazlab/gaia-skills` in place of
`uw-ssec/savvy`. They were tested on savvy's plugins, not on these. Where an assistant doesn't
load agents, the skill an agent preloads still works on its own.

## Troubleshooting

| Problem | Try |
| --- | --- |
| The skill doesn't load | Name it in your request. Check it's installed (`/skills`). If it still doesn't load for a reasonable request, open an issue: its description needs work |
| You can't find an agent | Run `claude plugin details <plugin>@gaia-skills` to see its agents. A new plugin loads in your next session, or after `/reload-plugins`. Agents load only in Claude Code, Cursor and Antigravity CLI |
| Install says the plugin isn't found | Run `claude plugin marketplace update gaia-skills`, then check the name against the [catalog](catalog.md) |
| A fix was merged but you don't see it | Run `claude plugin update <plugin>@gaia-skills`. If nothing changes, the maintainer didn't bump the version; tell them in an issue |
| `/plugin` Errors tab says a plugin "isn't installed here" | The project enables it but you haven't installed it: `claude plugin install <plugin>@gaia-skills --scope project` |
| A skill gives wrong instructions (dead endpoint, wrong variable name, outdated package) | Open an issue and mention the maintainer listed in the [catalog](catalog.md) |
| A plugin asks you to turn off permission prompts, send credentials somewhere, or hide what it does | Stop, don't follow it, and report it privately (below) |

## Get help or report a problem

- **Bugs and requests:** open an [issue](https://github.com/gaia-hazlab/gaia-skills/issues) and
  mention the plugin's maintainer. The **New skill or agent idea** template is for skills you
  wish existed.
- **Security problems** (a plugin that could leak data or credentials, run something
  destructive, or bypass your permissions): report privately through **Report a
  vulnerability** on the repository's Security tab, as described in
  [SECURITY.md](../SECURITY.md). Don't open a public issue.
