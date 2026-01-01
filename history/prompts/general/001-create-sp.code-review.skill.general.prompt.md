---
id: "001"
title: "Create sp.code-review skill"
stage: "general"
date: "2025-12-30"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: ""
user: ""
command: "Write skill file to .claude/commands/sp.code-review.md"
labels: ["skill","code-review","quality-gate"]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - .claude/commands/sp.code-review.md
  - .specify/templates/phr-template.prompt.md
tests:
  - "none"
---

## Prompt

Create a new Skill for the Todo App Phase 1 project.

Skill Requirements:
- Purpose: Review Python CLI code against project constitution and SDD standards
- Validates Phase 1 constraints (Python, console app, in-memory, no external dependencies)
- Code quality and architecture compliance checks
- When to use: Pre-commit, post-implementation, code review checkpoints
- Must include: Purpose, When to use, Inputs, Step-by-step process, Failure handling
- Must be owned by a specific agent (python-cli-agent recommended)
- Must be reusable and deterministic
- No placeholders or generic text
- Production-quality Markdown only

## Response snapshot

Created production-quality code review skill at `.claude/commands/sp.code-review.md` with:
- 7-phase review process (Pre-Flight → Report)
- Constitution compliance checks (quality, testing, performance)
- Phase 1 constraints verification (Python-only, console, in-memory, no deps)
- CLI-specific quality checks (input validation, loop patterns, error handling)
- Structured report output with critical/warning/info classifications
- Clear failure handling for all scenarios
- Owned by python-cli-agent for CLI code quality
- Deterministic behavior for consistent results

## Outcome

- ✅ Impact: New reusable skill for code review against constitution/SDD standards
- 🧪 Tests: None (skill definition, not implementation)
- 📁 Files: 1 created (.claude/commands/sp.code-review.md)
- 🔁 Next prompts: Use /sp.code-review after implementation tasks
- 🧠 Reflection: Skill fills quality gate gap in SDD workflow

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and PASS
- Prompt variant: "none"
- Next experiment: "none"
