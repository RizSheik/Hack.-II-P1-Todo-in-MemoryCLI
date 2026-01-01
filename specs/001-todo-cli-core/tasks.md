# Tasks: todo-cli-core

**Input**: Design documents from `/specs/001-todo-cli-core/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/cli-operations.md

**Organization**: Tasks grouped by user story for independent implementation/testing

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: User story label (US1, US2, US3, US4)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create project structure per implementation plan

- [x] T001 Create todo.py main entry point with `if __name__ == "__main__":` guard
- [x] T002 Create tests/ directory structure with conftest.py

---

## Phase 2: Foundational (Core Entity)

**Purpose**: Task entity that ALL user stories depend on

**CRITICAL**: Complete before ANY user story work

- [x] T003 [P] Create Status enum in todo.py (PENDING, COMPLETED)
- [x] T004 [P] Create Task dataclass in todo.py with id, title, description, status, created_at

**Checkpoint**: Task entity ready - user story implementation can begin

---

## Phase 3: User Story 1 - Add and List Tasks (Priority: P1) MVP

**Goal**: Users can add tasks and view them in a list

**Independent Test**: Run todo.py, add 2-3 tasks, verify they appear in list correctly

- [x] T005 [US1] Implement get_next_id() helper in todo.py (uses tasks list)
- [x] T006 [US1] Implement add_task() function in todo.py (validates title, creates Task)
- [x] T007 [US1] Implement list_tasks() function in todo.py (displays all tasks, handles empty list)
- [x] T008 [US1] Connect add/list to main menu in todo.py

**Checkpoint**: User Story 1 complete - basic todo app functional

---

## Phase 4: User Story 2 - Complete Tasks (Priority: P1)

**Goal**: Users can mark tasks as complete

**Independent Test**: Add tasks, complete one, verify status changes in list

- [x] T009 [US2] Implement complete_task() function in todo.py (finds by ID, updates status)
- [x] T010 [US2] Handle idempotent complete (already complete = silent success)
- [x] T011 [US2] Handle invalid ID error (Task not found)
- [x] T012 [US2] Connect complete to main menu in todo.py

**Checkpoint**: User Stories 1 + 2 complete - core CRUD functional

---

## Phase 5: User Story 3 - Delete Tasks (Priority: P2)

**Goal**: Users can remove tasks by ID

**Independent Test**: Add tasks, delete one, verify it no longer appears

- [x] T013 [US3] Implement delete_task() function in todo.py (finds by ID, removes from list)
- [x] T014 [US3] Add confirmation prompt before deletion
- [x] T015 [US3] Handle invalid ID error (Task not found)
- [x] T016 [US3] Connect delete to main menu in todo.py

**Checkpoint**: User Stories 1-3 complete - all P1 features done

---

## Phase 6: User Story 4 - Update Tasks (Priority: P2)

**Goal**: Users can edit task titles

**Independent Test**: Add task, update title, verify new title in list

- [x] T017 [US4] Implement update_task() function in todo.py (finds by ID, updates title)
- [x] T018 [US4] Handle empty title validation
- [x] T019 [US4] Handle invalid ID error (Task not found)
- [x] T020 [US4] Connect update to main menu in todo.py

**Checkpoint**: All 4 user stories complete

---

## Phase 7: Polish & Cross-Cutting Concerns

- [x] T021 Add Ctrl+C (KeyboardInterrupt) handling for graceful exit
- [x] T022 Validate menu input (1-6 range, handle invalid numbers)
- [x] T023 Add exit option (6 or 'q'/'quit')
- [x] T024 Verify quickstart.md workflow works end-to-end

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Phase 1: Setup | None | Phase 2 |
| Phase 2: Foundational | Phase 1 | Phases 3+ |
| Phase 3: US1 | Phase 2 | Polish |
| Phase 4: US2 | Phase 2 | Polish |
| Phase 5: US3 | Phase 2 | Polish |
| Phase 6: US4 | Phase 2 | Polish |
| Phase 7: Polish | All stories | None |

### User Story Dependencies

| Story | Priority | Depends On | Independent Test |
|-------|----------|------------|------------------|
| US1: Add/List | P1 | Foundational | Add → List = 2 tasks visible |
| US2: Complete | P1 | Foundational | Add → Complete → List = 1 pending |
| US3: Delete | P2 | Foundational | Add → Delete → List = 0 tasks |
| US4: Update | P2 | Foundational | Add → Update → List = new title |

### Parallel Opportunities

- Phase 1: T001, T002 can run in parallel
- Phase 2: T003, T004 can run in parallel
- Phases 3-6: Stories are independent after Phase 2
  - Can run in parallel (multiple developers)
  - Or sequentially: US1 → US2 → US3 → US4

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: US1
4. **STOP and VALIDATE**: Test add/list independently
5. Demo if ready (minimal viable product)

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. US1 → Test independently → Demo (MVP!)
3. US2 → Test independently → Demo
4. US3 → Test independently → Demo
5. US4 → Test independently → Demo
6. Polish → Final demo

---

## Summary

| Metric | Value |
|--------|-------|
| Total Tasks | 24 |
| Parallelizable [P] | 5 |
| Phases | 7 |
| User Stories | 4 |
| MVP Tasks | 8 (Phases 1-3) |

### Quick Start

**Minimal viable product (US1 only)**:
```
T001 → T002 → T003 → T004 → T005 → T006 → T007 → T008
```

**All features**:
```
T001 → T002 → T003 → T004 → T005 → T006 → T007 → T008 → T009 → T010 → T011 → T012 → T013 → T014 → T015 → T016 → T017 → T018 → T019 → T020 → T021 → T022 → T023 → T024
```
