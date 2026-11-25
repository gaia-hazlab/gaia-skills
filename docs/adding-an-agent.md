# Adding your agent to gaia-skills

This guide walks a GAIA group member through adding an agent (a Claude Code subagent) to this
repository, from an empty branch to a merged pull request. It takes about an hour the first
time, most of it spent writing the instructions.

## Skill, agent or command?

Most people want both a skill and an agent. Decide what each holds before writing.

| Piece | What it is | Use it for | Loads in |
| --- | --- | --- | --- |
| **Skill** (`skills/<name>/SKILL.md`) | Know-how the main conversation loads when a request matches its description | The method itself: steps, commands, conventions, checks | Claude Code, Copilot, Codex, Cursor, OpenCode |
| **Agent** (`agents/<name>.md`) | A separate Claude with its own instructions, tool limits and context window, which the main conversation hands a task to | A self-contained job with a clear input and output: build a stack, screen a catalogue, review a plugin | Claude Code, Cursor, Antigravity CLI |
| **Command** (`commands/<name>.md`) | A `/slash-command` a user types | A fixed prompt you run often | Claude Code, Cursor |

Put the know-how in a skill and have the agent preload it. Then people on Copilot or Codex
still get the method, and the agent stays short: its file says *how to behave*, the skill says
*how to do the science*.

## Before you start

- [pixi](https://pixi.sh) and [Claude Code](https://docs.claude.com/en/docs/claude-code) installed.
- A clone of this repository and a new branch:

  ```bash
  git clone https://github.com/gaia-hazlab/gaia-skills.git
  cd gaia-skills
  git switch -c add-<your-agent-name>
  pixi install -e ci
  ```

- The material the agent should work from: your notebook, script, README or processing notes.
  Write down three or four requests a colleague would type when they need this agent.

## Path A: a new skill and its agent (most common)

One command creates both, plus your plugin if it doesn't exist yet:

```bash
pixi run new-skill <plugin> <skill> --agent <agent> --maintainer @your-github-handle
```

For example:

```bash
pixi run new-skill gaia-seismic-landslides picking-landslide-signals \
  --agent landslide-signal-picker --maintainer @your-github-handle
```

This writes:

```text
community-plugins/gaia-seismic-landslides/
├── plugin.json                              # fill in the description
├── README.md                                # fill in
├── LICENSE
├── skills/picking-landslide-signals/SKILL.md    # fill in
└── agents/landslide-signal-picker.md            # fill in
```

and registers the plugin in `.claude-plugin/marketplace.json` and `docs/catalog.yml`. Every
placeholder is marked `TODO(scaffold)`. List them with:

```bash
pixi run scaffold-check
```

Fill in the skill first (see [CONTRIBUTING.md](../CONTRIBUTING.md) and the
`authoring-gaia-skills` skill), then the agent as described below.

## Path B: an agent for a skill that already exists

The scaffolder always creates a skill, so add an agent on its own by hand. Create
`<plugin-dir>/agents/<agent>.md` from the template in the next section, setting `skills:` to
the existing skill's name, then regenerate the catalog:

```bash
pixi run sync
```

## Writing the agent file

### Frontmatter

```markdown
---
name: landslide-signal-picker
description: >-
  Use this agent when the user wants candidate landslide signals picked from
  continuous seismic data for a station list and time window. It proposes the
  stations, filters and window, waits for approval, runs the picking workflow
  from the picking-landslide-signals skill, and returns a table of picks with
  the figures it made.
model: inherit
tools: Read, Grep, Glob, Bash, Write
skills:
  - picking-landslide-signals
---
```

| Field | Required | What to write |
| --- | --- | --- |
| `name` | yes | Lowercase with hyphens, the same as the file name without `.md`. Name the job, not yourself or your project |
| `description` | yes | When the main conversation should hand work to this agent, and what it returns. This is all Claude reads when deciding to delegate, so name the task, the data and the output. Start with "Use this agent when ..." |
| `model` | no | `inherit` (use whatever model the user runs). Leave it unless you have tested another |
| `tools` | no | Leave it out to give the agent the same tools as the main conversation. Set it to restrict the agent, e.g. `Read, Grep, Glob` for a read-only reviewer. If you include `Bash`, say why in the pull request |
| `skills` | no, but recommended | A YAML **list** of skill names to preload, even if there is only one. A plain string breaks the agent in Copilot CLI and fails `pixi run check-all` |

### Body

The body is the agent's system prompt. It doesn't see your conversation with the user, only the
task handed to it, so it must stand on its own. Cover, in this order:

1. **Role and goal**, in one or two sentences.
2. **Inputs it expects** and what to do when one is missing (ask, or stop and report).
3. **Steps**, pointing to the preloaded skill for the method rather than repeating it.
4. **What it must ask before doing.** For GAIA this always includes: large downloads (1 GB is a
   sensible default threshold; the skill can set its own), anything that uses an HPC allocation or cloud credits, writing outside the project
   directory, and deleting anything.
5. **What it returns**: the files it wrote and where, a short summary, and what it could not
   verify.

Example:

```markdown
You pick candidate landslide signals from continuous seismic data for GAIA HazLab.

Inputs: a station list (network.station), a time window in UTC, and an output directory.
If any is missing, ask for it before doing anything else.

1. Propose the data request (stations, channels, window, data center) and the filter and
   detector settings from the picking-landslide-signals skill. Wait for the user to approve.
2. Estimate the download size. Above 1 GB, report the estimate and ask before fetching.
3. Run the workflow in the skill. Write outputs only to the output directory.
4. Check each pick against the skill's verification step and drop the ones that fail.

Return: the path to the picks table, the figures you made, how many candidates passed and
failed the checks, and anything you could not verify.

Never put credentials in a file or command line; read them from the environment variables the
skill names.
```

### Rules that apply to every agent

- No credentials, tokens, private URLs, unpublished data paths or personal information,
  including in examples.
- Nothing that tells the agent to skip permission prompts, change the user's settings, or hide
  what it does. The [security checklist](../CONTRIBUTING.md#security-review-checklist) applies
  to agents exactly as to skills.
- Name every command or script the agent may run, and why it needs the network, in your
  plugin's `README.md`.

## Test it

**1. Run the checks.** Both must pass before you open a pull request.

```bash
pixi run sync
pixi run check-all
```

**2. Try it in Claude Code** with only your plugin loaded:

```bash
claude --plugin-dir community-plugins/<plugin>
```

First check that Claude Code sees the agent. In a terminal:

```bash
claude --plugin-dir community-plugins/<plugin> plugin details <plugin>
```

Your agent should appear under **Agents** in the component inventory. Inside a session it is
named `<plugin>:<agent>`. Then, inside that session:

- Ask for it by name: *"Use the landslide-signal-picker agent to pick signals at two Mount
  Rainier stations for March 2025."* It should start with its proposal and wait for you.
- Then ask without naming it, the way a colleague would. Don't expect this to delegate every
  time: Claude decides for itself, and for a small task it often just does the work in the
  main conversation. That is fine as long as the preloaded skill loads. For a long or
  multi-step job, if Claude never picks the agent, make the `description` name the task, the
  data and the output more concretely. Tell users to name the agent when they want it for
  sure.

**3. Optional headless check**, useful when you are tuning the description. This runs one
request and prints which agent, if any, Claude handed it to:

```bash
claude -p "<a request a colleague would type>" \
  --plugin-dir community-plugins/<plugin> \
  --output-format stream-json --verbose --max-turns 2 --no-session-persistence \
  | jq -c 'select(.type=="assistant" and .parent_tool_use_id==null)
           | .message.content[]? | select(.type=="tool_use" and .name=="Agent")
           | .input.subagent_type'
```

It prints `"<plugin>:<agent>"` when the agent was chosen and nothing when it wasn't. Results
vary between runs, so run it two or three times. Once the agent is chosen it runs to the end
(the two-turn cap applies only to the main conversation), so a run can take several minutes.
A non-zero exit status only means the cap was reached.

## Open the pull request

```bash
git add -A
git commit -m "Add <agent> agent to <plugin>"
git push -u origin HEAD
gh pr create
```

Fill in the pull request template: what the agent may run, how you tested it, and which parts an
AI assistant wrote. Before asking for review, run the reviewer agent from `gaia-core` on your
plugin (install it with `claude plugin install gaia-core@gaia-skills`):

`Use the skill-reviewer agent to review community-plugins/<plugin>`

Fix what it finds, then request a review. A maintainer checks the pull request against the
security checklist before merging.

## When something fails

| Message or symptom | Fix |
| --- | --- |
| `skills must be a YAML list of names` | Write `skills:` then `  - skill-name` on the next line, not `skills: skill-name` |
| `scaffold placeholder(s) left` | Run `pixi run scaffold-check` and replace each listed `TODO(scaffold)` |
| `docs/catalog.md is out of date` or manifest drift | Run `pixi run sync` and commit the changed files |
| `description` length error (skills) | 100 to 1024 characters: say what it does, then "Use when ..." with real phrasings |
| Agent missing from the `plugin details` inventory | File must be in `<plugin-dir>/agents/`, end in `.md`, and start with a `---` frontmatter block |
| Claude doesn't delegate unless the agent is named | Normal for small tasks. For long jobs, make `description` say concretely when to use it and what it returns, naming the data and tools users mention |
| Agent works in Claude Code but colleagues on Copilot get nothing | Expected: Copilot and Codex don't load agents. Make sure the method is in the skill |

Questions: open an issue with the **New skill or agent idea** template, or ask in the GAIA
channel.
