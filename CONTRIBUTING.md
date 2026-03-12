# Contributing to gaia-skills

Thank you for contributing to the gaia-skills template repository. This guide explains how to add new personas, skill files, and culture documents.

## General Principles

- Write in plain, clear markdown that is readable by both humans and AI agents.
- Keep each file focused on a single topic, persona, or practice.
- Follow the templates provided in each directory.
- Use lowercase, hyphenated filenames (e.g., `field-geologist.md`, `data-management.md`).

## Adding a Persona

1. Copy `personas/_template.md` to a new file in `personas/`.
2. Fill in all front-matter fields and section headings.
3. Describe the persona's goals, knowledge areas, tools, and collaboration patterns.
4. Open a pull request with a short description of the new persona.

## Adding a Skill

1. Identify the appropriate discipline sub-folder under `skills/`.
2. Copy `skills/_template.md` into the sub-folder.
3. Name the file after the specific skill or topic (e.g., `electrical-resistivity-tomography.md`).
4. Fill in all sections: overview, prerequisites, tools, workflow, and references.
5. Open a pull request.

## Adding a Culture Document

1. Choose the correct category under `culture/`:
   - `culture/open-science/` — principles and constraints for practising open science
   - `culture/data-management/` — data lifecycle and FAIR data practices
   - `culture/modeling/` — modelling workflows, uncertainty, and reproducibility
2. Copy the relevant template file (e.g., `culture/open-science/_template.md`).
3. Name the file descriptively (e.g., `reproducibility.md`, `metadata-standards.md`).
4. Open a pull request.

## Pull Request Checklist

- [ ] File uses a lowercase hyphenated name
- [ ] All front-matter fields are populated
- [ ] All template section headings are present
- [ ] Spelling and grammar have been checked
- [ ] No sensitive data or credentials are included
