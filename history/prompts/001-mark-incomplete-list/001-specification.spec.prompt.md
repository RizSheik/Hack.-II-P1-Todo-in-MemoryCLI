---
id: "001"
title: "Todo Enhancement Specification"
stage: "spec"
date: "2026-01-01"
surface: "agent"
model: "sonnet-4-5-20250929"
feature: "mark-incomplete-list"
branch: "001-mark-incomplete-list"
user: "human"
command: "/sp.specify"
labels: ["todo-app","enhancement","specification"]
links:
  spec: "specs/001-mark-incomplete-list/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "specs/001-mark-incomplete-list/spec.md"
  - "specs/001-mark-incomplete-list/checklists/requirements.md"
tests: []
---

## Prompt

Project: Todo App – Phase I (Console, In-Memory, Python)
Agent: todo-spec-manager (root), subagents: todo-domain-agent, python-cli-agent, hackathon-review-agent

Enhancement Features to Specify:
1. Mark Task Incomplete:
   - User can toggle a completed task back to pending
   - Input validation for task id
   - Edge case: already pending task
   - Update status field in Task dataclass

2. Improved List View:
   - Show tasks in **tabular format**
   - Include: ID, Title, Status (PENDING/COMPLETED), Created At
   - Highlight completed tasks visually (e.g.,  for complete,  for pending)
   - Sort tasks by created_at by default
   - Handle empty task list gracefully

Requirements:
- Specification must include: purpose, expected behavior, user inputs, edge cases, acceptance criteria.
- Phase I constraints apply: Python, CLI, in-memory only, synchronous, no database.
- Output in Markdown with structured sections for each enhancement.
- Include clear **Task IDs** for each enhancement (e.g., T025-T028)
- Validate with domain expert (todo-domain-agent) and judge brain (hackathon-review-agent)

Deliverable:
- Markdown specification for each enhancement with acceptance criteria and edge cases.

## Response snapshot

Created feature branch `001-mark-incomplete-list` and specification for two enhancements:
1. **Mark Task Incomplete** - Toggle completed tasks back to pending with input validation
2. **Improved List View** - Tabular display with ID, Title, Status, Created At; visual indicators; sorted by created_at

Specification includes:
- 4 user stories with Given/When/Then acceptance scenarios
- 10 functional requirements (FR-001 to FR-010)
- 5 measurable success criteria
- Edge cases: already pending, invalid input, empty list, long titles
- Validated by todo-domain-agent (APPROVED) and hackathon-review-agent (7/10 - CONDITIONAL GO)

## Outcome

- ✅ Impact: Created specification for Mark Task Incomplete and Improved List View features
- 🧪 Tests: No tests run during spec creation
- 📁 Files: Created spec.md and requirements.md checklist
- 🔁 Next prompts: `/sp.plan` or `/sp.tasks` to proceed to implementation planning
- 🧠 Reflection: Spec validation passed with minor feedback about FR-005 clarity (informational vs error message distinction)

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All checklist items passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
