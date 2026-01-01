# Tasks: Mark Task Incomplete & Improved List View

**Input**: Design documents from `/specs/001-mark-incomplete-list/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Tests**: Manual CLI verification + pytest (12 tests passing)

**Status**: ✅ ALL TASKS COMPLETED

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Existing Project)

**Purpose**: Verify existing project structure is ready for modifications

- [x] T025 Verify todo.py exists at repository root and runs without errors
- [x] T026 Review existing Task dataclass and Status enum in todo.py (lines 20-34)

---

## Phase 2: Foundational (Existing Infrastructure)

**Purpose**: Core infrastructure already in place - verify it's ready

- [x] T027 Confirm in-memory task storage `tasks: list[Task]` exists (line 38)
- [x] T028 Confirm get_next_id() function exists for ID generation (lines 41-45)

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Mark a Completed Task as Incomplete (Priority: P1) 🎯 MVP

**Goal**: Allow users to toggle a completed task back to pending status

**Independent Test**: Complete a task, then mark it incomplete, verify status changes and confirmation message displays

**Status**: ✅ COMPLETED (T029-T034)

### Implementation for User Story 1

- [x] T029 [US1] Add menu option "6" to show_menu() function in todo. Mark task incomplete.py:175
- [x] T030 [US1] Create uncomplete_task() function in todo.py with input validation for numeric task ID
- [x] T031 [US1] Implement task lookup and status toggle logic in uncomplete_task() (COMPLETED → PENDING)
- [x] T032 [US1] Add error handling for non-existent task ID with message: "Error: Task #X not found."
- [x] T033 [US1] Add edge case handling for already-pending task with message: "Task #X is already incomplete."
- [x] T034 [US1] Wire uncomplete_task() to menu option 6 in main() loop

**Checkpoint**: User Story 1 complete - test by completing a task then marking it incomplete

---

## Phase 4: User Story 2 - View Tasks in Tabular Format (Priority: P1)

**Goal**: Display tasks in clean tabular format with ID, Title, Status, Created At columns

**Independent Test**: Add tasks with different statuses and timestamps, run list command, verify tabular format

**Status**: ✅ COMPLETED (T035-T040)

### Implementation for User Story 2

- [x] T035 [US2] Modify list_tasks() function in todo.py:62 to sort tasks by created_at ascending
- [x] T036 [US2] Add timestamp formatting using strftime("%Y-%m-%d") for created_at display
- [x] T037 [US2] Create tabular column layout with headers: ID | Created | Status | Title
- [x] T038 [US2] Implement fixed-width columns: ID (3 chars), Created (11 chars), Status (7 chars)
- [x] T039 [US2] Add visual status indicators: [X] for COMPLETED, [ ] for PENDING
- [x] T040 [US2] Add title truncation for long titles (max 30 chars, append "..." if needed)

**Checkpoint**: User Story 2 complete - test by viewing list with mixed status tasks

---

## Phase 5: User Story 3 & 4 - Timestamps and Visual Indicators (Priority: P2)

**Goal**: Display task creation timestamps and clear visual status differentiation

**Independent Test**: Verify Created At column shows formatted timestamps and status indicators are consistent

**Status**: ✅ COMPLETED (T041-T042)

### Implementation for User Stories 3-4

- [x] T041 [US3] Verify timestamp formatting displays correctly (YYYY-MM-DD format)
- [x] T042 [US4] Verify visual status indicators ([X]/[ ]) distinguish completed from pending tasks

**Checkpoint**: User Stories 3-4 complete - verify in list view output

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Edge cases and user experience improvements

**Status**: ✅ COMPLETED (T043-T045)

- [x] T043 Verify empty task list displays friendly message (existing, line 65)
- [x] T044 Verify invalid numeric input shows error message (ValueError handling)
- [x] T045 Add summary line showing pending/completed counts (e.g., "Total: 3 tasks (2 pending, 1 completed)")

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately ✅
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories ✅
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion ✅
  - US1 (Mark Incomplete) and US2 (Tabular View) are independent - can run in parallel ✅
- **Polish (Phase 6)**: Depends on User Stories completion ✅

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories ✅
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories ✅
- **User Stories 3-4 (P2)**: Can start after User Story 2 (Phase 4) - depends on tabular view implementation ✅

### Within Each User Story

- Core implementation before edge cases ✅
- Story complete before moving to polish ✅

### Parallel Opportunities

- Phase 1 tasks can run in parallel ✅
- Phase 2 tasks can run in parallel ✅
- US1 (Phase 3) and US2 (Phase 4) can proceed in parallel since they modify different functions ✅

---

## Implementation Summary

| Metric | Value |
|--------|-------|
| Total Tasks | 21 |
| Completed | 21 ✅ |
| Setup Tasks | 2 ✅ |
| Foundational Tasks | 2 ✅ |
| US1 (Mark Incomplete) Tasks | 6 ✅ |
| US2 (Tabular View) Tasks | 6 ✅ |
| US3-4 Tasks | 2 ✅ |
| Polish Tasks | 3 ✅ |

### Test Results

```
============================= 12 passed in 0.10s ==============================
```

### Independent Test Criteria Verification

- **US1**: ✅ Can mark a completed task as incomplete and receive confirmation
- **US2**: ✅ Can view tasks in tabular format with proper sorting
- **US3**: ✅ Timestamps display in YYYY-MM-DD format
- **US4**: ✅ Visual indicators ([X]/[ ]) clearly show task status

### Suggested MVP Scope - DELIVERED

User Story 1 (Phase 3) delivered value - users can undo task completion. User Story 2 delivered improved display.

---

## Reference

- **Feature Spec**: `specs/001-mark-incomplete-list/spec.md`
- **Implementation Plan**: `specs/001-mark-incomplete-list/plan.md`
- **Data Model**: `specs/001-mark-incomplete-list/data-model.md`
- **Source File**: `todo.py` (repository root)
- **Tests**: `tests/test_task.py`
