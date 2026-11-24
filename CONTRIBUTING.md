# Contributing to gaia-skills

Every GAIA group member is welcome to add plugins here. This page covers how to add a skill,
the rules the checks enforce, and the security review every change gets before it merges.

## Add a skill in five steps

You need [pixi](https://pixi.sh) and a clone of this repository. Work on a branch.

1. **Install the tooling** (once):

   ```bash
   pixi install -e ci
   ```

2. **Scaffold.** Pick a plugin (your domain, e.g. `gaia-seismic-monitoring`) and a skill name
   that says the task (`picking-landslide-signals`). If the plugin doesn't exist yet the script
   creates it, with you as maintainer:

   ```bash
   pixi run new-skill <plugin> <skill> --maintainer @your-github-handle
   # --agent <name>  also create a subagent that preloads the skill
   # --core          only for cross-cutting GAIA tooling (ask the leads first)
   ```

   This writes `community-plugins/<plugin>/` with `plugin.json`, `README.md`, `LICENSE` and
   `skills/<skill>/SKILL.md`, and adds the plugin to `.claude-plugin/marketplace.json` and
   `docs/catalog.yml`.

3. **Fill every `TODO(scaffold)` marker**: the skill's `description` and body, the plugin
   `description` in `plugin.json`, the plugin README, and the `example:` prompt in
   `docs/catalog.yml`. The `authoring-gaia-skills` skill in `gaia-core` explains what makes a
   good description and body; with that plugin installed, ask Claude Code to help.

4. **Check and try it**:

   ```bash
   pixi run sync                      # regenerate manifests and docs/catalog.md
   pixi run check-all                 # the same gates CI runs
   claude --plugin-dir community-plugins/<plugin>
   ```

   In that Claude Code session, type your catalog example and confirm the skill loads. If it
   doesn't, rewrite the description.

5. **Open a pull request** and fill in the template. A maintainer reviews it against the
   security checklist below. The `skill-reviewer` agent in `gaia-core` runs most of that
   review; run it yourself first.

Adding an agent? [docs/adding-an-agent.md](docs/adding-an-agent.md) is the step-by-step guide.

## What a plugin looks like

```text
community-plugins/<plugin>/
├── plugin.json              # source manifest: edit this one
├── .claude-plugin/plugin.json   # generated, don't edit
├── README.md                # what it does, what it may run, maintainer
├── LICENSE                  # a real file, not a symlink
├── skills/<skill>/
│   ├── SKILL.md
│   ├── references/          # optional long material, linked from SKILL.md
│   └── scripts/             # optional helper scripts, executable
├── agents/<agent>.md        # optional, Claude Code / Cursor / Antigravity only
└── commands/<command>.md    # optional, Claude Code / Cursor only
```

## Rules the checks enforce

`pixi run check-all` fails on any of these. CI runs the same checks.

- **Generated files are current.** Edit only `<plugin>/plugin.json`, the plugin list in
  `.claude-plugin/marketplace.json` and `docs/catalog.yml`, then run `pixi run sync`. Never edit
  `.claude-plugin/plugin.json`, `.agents/plugins/marketplace.json`,
  `.cursor-plugin/marketplace.json` or `docs/catalog.md` by hand.
- **Skill frontmatter.** `name` equals the folder name; `description` is 100 to 1024
  characters. Optional `metadata` values must be strings (quote dates).
- **Self-contained skills.** Every file and relative link inside a skill stays inside that
  skill's folder, because clients install one skill folder at a time. Name a sibling skill in
  prose instead of linking to it.
- **Unique names.** Plugin and skill names are unique across the repository.
- **Agent `skills:` is a YAML list**, even for one skill.
- **`plugin.json` has a closed schema**: only `$schema`, `name`, `version`, `description`,
  `author`, `homepage`, `repository`, `license`, `keywords`, `extensions`.
- **No scaffold placeholders left** (`TODO(scaffold)`).
- **Catalog entry.** Every skill has an `example:` in `docs/catalog.yml`.

## Writing guidance

- Write for an agent that knows Python and geoscience but has never seen your workflow. Say
  what a newcomer would get wrong: units, CRS, time zones, station or product quirks, which
  check proves the result.
- Give exact commands, pinned package versions and official endpoints. Don't let the skill guess.
- Never put credentials, tokens, private URLs, unpublished data paths or personal information
  in a skill, including examples. Say which environment variable holds a credential instead.
- Keep `SKILL.md` under about 500 lines; move the rest to `references/`.
- An agent should ask before large downloads, writes outside the project, or anything that
  spends money or an HPC allocation. Say so in the skill.

## Security review checklist

Agents act on the text in a plugin: they run the commands it suggests, open the URLs it links
to and follow its instructions. A harmful instruction is as dangerous as harmful code, so a
maintainer checks every pull request that adds or changes a plugin against this list. Authors
should check it first. Adapted from savvy's
[security review checklist](https://github.com/uw-ssec/savvy/blob/main/CONTRIBUTING.md#-security-review-checklist).

Review the raw files, not GitHub's rendered view, which hides HTML comments. From the
repository root:

```bash
rg -n --hidden "allowed-tools|curl|wget|\| *(ba|z)?sh|sudo|rm -rf|https?://|<!--|base64|ignore (all|previous)" <plugin-dir>
rg -n --hidden -P "[\x{200B}-\x{200F}\x{202A}-\x{202E}\x{2060}-\x{2064}\x{FEFF}]" <plugin-dir>   # should print nothing
```

**Shell commands**

- [ ] Every command the plugin tells the agent to run is one a careful user would run
      themselves, shown in the text rather than built at run time.
- [ ] Nothing pipes a download into a shell unless it is the tool's official installer, and the
      agent is told to confirm with the user first.
- [ ] Nothing deletes files outside the project, uses `sudo`, or changes shell profiles, SSH
      keys, Git configuration or security tools.
- [ ] Bundled scripts do what the skill says, touch only paths the user gives them, and use the
      network only for a destination the user asked for.
- [ ] Tool grants (`allowed-tools`, `tools`) list only what the task needs. A pre-approved
      `Bash` grant is explained in the pull request.

**External URLs and data**

- [ ] Every link goes where its text says, to an official source (the data provider, the
      project's documentation or repository, the package index).
- [ ] Nothing tells the agent to send code, data, environment variables or credentials to a
      URL, or to fetch and follow instructions from one.
- [ ] Downloads, container images and packages are pinned where the format allows.
- [ ] Each MCP server is named in the plugin README with the command it starts and who
      maintains it.

**Instructions that override agent safeguards**

- [ ] Nothing tells the agent to skip permission prompts, switch to an auto-approve mode, or edit
      the user's agent settings, permission rules or hooks.
- [ ] Nothing tells the agent to ignore the user's instructions or `AGENTS.md` / `CLAUDE.md`
      files, or to claim authority it doesn't have.
- [ ] Nothing tells the agent to hide what it is doing or act outside the task asked for.
- [ ] Reference material reads as information, not orders.
- [ ] No hidden text: no instructions in HTML comments, no invisible Unicode, no encoded payloads.

**Everything else**

- [ ] No credentials, tokens, private URLs, unpublished data locations or personal data.
- [ ] The plugin README says what the plugin does, what it may run, and why it needs the network.

If a check fails, ask for a change. Don't merge with a note to fix later. Report anything that
looks deliberately malicious privately as described in [SECURITY.md](SECURITY.md).

## Changelog and versions

Add a line to [CHANGELOG.md](CHANGELOG.md) under `## [Unreleased]` for the plugin you changed.
Bump a plugin's `version` in its `plugin.json` when you change its behaviour (patch for fixes,
minor for new skills), then run `pixi run sync`.

## AI-assisted contributions

Using an agent to write a skill is expected. You still own every line: read the full diff, run
the checks yourself, and say in the pull request which parts were generated.
