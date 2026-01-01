---
id: "todo-cli-core-001"
title: "Todo CLI Core specification"
stage: "spec"
date: "2025-12-30"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "todo-cli-core"
branch: "001-todo-cli-core"
user: ""
command: "/sp.specify todo-cli-core"
labels: ["specification","todo-app","cli","core-features"]
links:
  spec: "specs/001-todo-cli-core/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - specs/001-todo-cli-core/spec.md
  - specs/001-todo-cli-core/checklists/requirements.md
tests:
  - "none"
---

## Prompt

todo-cli-core

## Response snapshot

Created feature specification for todo-cli-core at `specs/001-todo-cli-core/spec.md`:

**User Stories (4 total)**:
- P1: Add and List Tasks (core fundamental functionality)
- P1: Complete Tasks (core functionality for progress tracking)
- P2: Delete Tasks (important for list management)
- P2: Update Tasks (useful for maintenance)

**Functional Requirements (11 total)**:
- FR-001 to FR-011 covering all 5 operations (Add/List/Complete/Delete/Update)
- Input validation (non-empty titles, valid IDs)
- User-friendly error messages
- Menu return behavior

**Key Entity**: Task with id, title, description, status, created_at

**Success Criteria (6 total)**:
- SC-001: Add task and see in list within 10 seconds
- SC-002: All 5 operations work correctly
- SC-003: List displays 10+ tasks correctly
- SC-004: Invalid inputs show clear errors
- SC-005: Happy path complete in under 2 minutes
- SC-006: Deterministic behavior

**Edge Cases (6 total)**: Empty list, empty title, duplicate titles, invalid IDs, re-completing, deleting completed

**Out of Scope**: Persistence, multiple lists, tags, due dates, search, undo, export, auth

**Quality Checklist**: 16/16 items passed - specification ready for planning

## Outcome

- ✅ Impact: Core todo CLI specification with 5 operations defined
- 🧪 Tests: None (specification, tests created during implementation)
- 📁 Files: 1 created (specs/001-todo-cli-core/spec.md), 1 checklist (checklists/requirements.md)
- 🔁 Next prompts: /sp.clarify (if needed) or /sp.plan for implementation planning
- 🧠 Reflection: Specification follows SDD principles with testable requirements

## Evaluation notes (flywheel)

- Failure modes observed: "none"
- Graders run and PASS (16/16 checklist items)
- Prompt variant: "none"
- Next experiment: "none"
