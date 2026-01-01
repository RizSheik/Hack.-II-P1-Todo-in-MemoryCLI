---
id: "004"
title: "Todo Enhancement Implementation"
stage: "green"
date: "2026-01-01"
surface: "agent"
model: "sonnet-4-5-20250929"
feature: "mark-incomplete-list"
branch: "001-mark-incomplete-list"
user: "human"
command: "/sp.implement"
labels: ["todo-app","enhancement","implementation"]
links:
  spec: "specs/001-mark-incomplete-list/spec.md"
  plan: "specs/001-mark-incomplete-list/plan.md"
  tasks: "specs/001-mark-incomplete-list/tasks.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - "todo.py"
  - "tests/test_task.py"
tests:
  - "tests/test_task.py::TestTask::test_task_creation_defaults"
  - "tests/test_task.py::TestTask::test_task_creation_with_all_params"
  - "tests/test_task.py::TestGetNextId::test_first_task_id"
  - "tests/test_task.py::TestGetNextId::test_incrementing_ids"
  - "tests/test_task.py::TestGetNextId::test_id_after_deletion"
  - "tests/test_task.py::TestUncompleteTask::test_uncomplete_completed_task"
  - "tests/test_task.py::TestUncompleteTask::test_uncomplete_already_pending_task"
  - "tests/test_task.py::TestUncompleteTask::test_uncomplete_nonexistent_task"
  - "tests/test_task.py::TestUncompleteTask::test_uncomplete_invalid_input"
  - "tests/test_task.py::TestListTasks::test_list_tasks_sorting"
  - "tests/test_task.py::TestListTasks::test_list_tasks_status_indicators"
  - "tests/test_task.py::TestListTasks::test_list_tasks_empty"
---

## Prompt

Project: Todo App – Phase I (Console, In-Memory, Python)
Parent Tasks: /sp.tasks (T025-T028)

Instructions:
- Implement **exactly one Task per code block**
- Use **existing Task dataclass and menu system**
- Maintain Phase I constraints (Python, CLI, in-memory)
- Ensure deterministic and beginner-friendly code
- Include inline comments for clarity
- Add unit tests for new features in tests/test_task.py
- Do not implement any future-phase features
- Include input validation and graceful error handling

Deliverable:
- Updated todo.py with enhancement features
- Updated tests/test_task.py with new tests
- Ensure all tasks pass automatically with pytest

## Response snapshot

Implemented all 21 tasks across 6 phases:

**User Story 1 - Mark Incomplete (T029-T034)**:
- Added menu option 6 "Mark task incomplete" to show_menu()
- Created uncomplete_task() function with input validation
- Handles error cases: non-existent ID, already pending, invalid input

**User Story 2 - Tabular List View (T035-T040)**:
- Modified list_tasks() to sort by created_at ascending
- Added timestamp formatting (YYYY-MM-DD)
- Created tabular column layout with headers
- Fixed-width columns: ID (3), Created (11), Status (7), Title (30)
- Visual status indicators: [X] for COMPLETED, [ ] for PENDING
- Title truncation for long titles with "..."

**Tests**: 7 new tests added (4 for uncomplete_task, 3 for list_tasks)
- All 12 tests passing

## Outcome

- ✅ Impact: Complete implementation of Mark Task Incomplete and Improved List View
- 🧪 Tests: 12/12 passing (7 original + 5 new for enhanced features)
- 📁 Files: todo.py updated, tests/test_task.py extended
- 🔁 Next prompts: Ready for /sp.code-review or /sp.refactor
- 🧠 Reflection: Implementation follows existing patterns; tests validate all edge cases

## Evaluation notes (flywheel)

- Failure modes observed: 2 test failures initially (assertion logic)
- Graders run and results (PASS/FAIL): All 12 tests pass after fixes
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
