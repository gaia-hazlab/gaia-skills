# Writing a subagent

A subagent is a Markdown file in `<plugin>/agents/<name>.md`. Claude Code, Cursor and
Antigravity CLI load agents; Copilot, Codex and OpenCode do not, so anything every client needs
belongs in a skill and the agent should preload that skill.

```markdown
---
name: insar-stack-builder
description: >-
  Use this agent when the user needs an InSAR time-series stack built from HyP3
  products for a region and date range. It proposes the configuration, waits for
  approval, then writes and runs the staging script.
model: inherit
skills:
  - staging-insar-stacks
---

You are ... (goal, inputs, outputs, what you must ask before doing)
```

Rules the checks enforce or reviewers look for:

- `skills:` is a YAML list even for one skill. Copilot CLI silently drops an agent whose
  `skills` is a string.
- `description` says when the main conversation should hand work to this agent. Include one or
  two `<example>` blocks if the trigger is subtle.
- Add `tools:` only to restrict the agent (for example `tools: Read, Grep, Glob` for a
  read-only reviewer). Explain in the pull request any agent that needs `Bash`.
- The body states what the agent must ask the user before doing: large downloads, writes
  outside the project, anything that costs money or uses an allocation.
