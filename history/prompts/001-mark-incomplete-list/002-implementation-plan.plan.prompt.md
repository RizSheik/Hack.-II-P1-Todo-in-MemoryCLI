---
id: "002"
title: "Todo Enhancement Implementation Plan"
stage: "plan"
date: "2026-01-01"
surface: "agent"
model: "sonnet-4-5-20250929"
feature: "mark-incomplete-list"
branch: "001-mark-incomplete-list"
user: "human"
command: "/sp.plan"
labels: ["todo-app","enhancement","planning"]
links:
  spec: "specs/001-mark-incomplete-list/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "specs/001-mark-incomplete-list/plan.md"
  - "specs/001-mark-incomplete-list/research.md"
  - "specs/001-mark-incomplete-list/data-model.md"
tests: []
---

## Prompt

Project: Todo App – Phase I (Console, In-Memory, Python)
Agent: python-cli-agent
Parent Spec: /sp.specify (Mark Task Incomplete, Improved List View)

Instructions:
1. Break each enhancement feature into **small, implementable steps**
2. Assign **Task IDs** to each step
3. Include **CLI flow recommendations** for each operation
4. Specify **error handling** for invalid inputs
5. Recommend **print layout** for improved list view
6. Follow Phase I constraints: CLI, Python, in-memory only

Deliverable:
- Markdown plan with step-by-step actions for each Task ID
- Clearly indicate which sub-agent executes what (Python CLI agent)
- Keep plan deterministic and beginner-friendly

## Response snapshot

Created implementation plan with 4 tasks (T025-T028):

1. **T025**: Add "Mark Incomplete" menu option (show_menu modification)
2. **T026**: Implement uncomplete_task() function (status toggle logic)
3. **T027**: Enhance list_tasks() with tabular format (columns, sorting, status indicators)
4. **T028**: Handle edge cases (empty list, long titles, invalid input)

Technical decisions documented:
- Menu option 7 for "Mark Incomplete"
- Timestamp format: YYYY-MM-DD HH:MM
- Status indicators: [X] / [ ]
- Fixed-width columns with truncation
- Sort by created_at ascending

## Outcome

- ✅ Impact: Implementation plan ready for /sp.tasks generation
- 🧪 Tests: No tests run during planning
- 📁 Files: plan.md, research.md, data-model.md created
- 🔁 Next prompts: /sp.tasks to generate task breakdown
- 🧠 Reflection: All Phase I constraints satisfied; no over-engineering

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All Constitution checks passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
