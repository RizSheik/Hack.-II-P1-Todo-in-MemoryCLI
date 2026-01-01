# Feature Specification: Todo CLI Core

**Feature Branch**: `001-todo-cli-core`
**Created**: 2025-12-30
**Status**: Draft
**Input**: User description: "todo-cli-core"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add and List Tasks (Priority: P1)

As a user, I want to add new tasks with titles and see a list of all my tasks so that I can track what I need to do.

**Why this priority**: Core fundamental functionality. Without adding and listing tasks, there is no todo application.

**Independent Test**: Can be fully tested by running the CLI, adding 2-3 tasks, and verifying they all appear in the list with correct information.

**Acceptance Scenarios**:

1. **Given** the task list is empty, **When** the user adds a task "Buy milk", **Then** the task appears in the list with status "pending"
2. **Given** the user has 2 pending tasks, **When** the user adds a task "Pay bills", **Then** the list shows all 3 tasks
3. **Given** the user adds a task with a title and description, **When** the user lists tasks, **Then** both title and description are displayed

---

### User Story 2 - Complete Tasks (Priority: P1)

As a user, I want to mark tasks as complete so that I can track my progress on what I have finished.

**Why this priority**: Core functionality for todo apps. Users need to know what is done vs. what remains.

**Independent Test**: Can be fully tested by adding tasks, marking one as complete, and verifying only the remaining tasks show as pending.

**Acceptance Scenarios**:

1. **Given** the user has a pending task, **When** the user marks it as complete, **Then** the task status changes to "completed"
2. **Given** the user has 2 pending and 1 completed task, **When** the user marks another task complete, **Then** the list shows 1 pending and 2 completed
3. **Given** the user has completed tasks, **When** the user lists tasks, **Then** completed tasks are visually distinguished from pending tasks

---

### User Story 3 - Delete Tasks (Priority: P2)

As a user, I want to remove tasks that are no longer needed so that my task list stays relevant.

**Why this priority**: Important for list management but not essential for MVP. Users can complete tasks instead of deleting them.

**Independent Test**: Can be fully tested by adding tasks, deleting one, and verifying it no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** the user has 3 tasks, **When** the user deletes task #2, **Then** the list shows only tasks #1 and #3
2. **Given** the user attempts to delete a non-existent task, **Then** an error message is displayed

---

### User Story 4 - Update Tasks (Priority: P2)

As a user, I want to edit task titles or descriptions so that I can correct mistakes or refine my task details.

**Why this priority**: Useful for maintenance but not essential for MVP. Users can delete and re-add tasks if needed.

**Independent Test**: Can be fully tested by adding a task, updating its title, and verifying the new title appears in the list.

**Acceptance Scenarios**:

1. **Given** the user has a task titled "Buy mil", **When** the user updates it to "Buy milk", **Then** the task shows "Buy milk" in the list
2. **Given** the user attempts to update a non-existent task, **Then** an error message is displayed

---

### Edge Cases

- **Empty task list**: When listing tasks with no tasks added, display a clear "No tasks" message
- **Empty title**: Reject tasks with empty or whitespace-only titles
- **Duplicate titles**: Allow duplicate titles (Phase I does not enforce uniqueness)
- **Invalid task ID**: Display user-friendly error when referencing non-existent task
- **Re-completing task**: Marking an already-completed task as complete again should succeed silently (idempotent)
- **Deleting completed task**: Allow deletion of completed tasks

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with a title (description optional)
- **FR-002**: System MUST validate that task titles are not empty or whitespace-only
- **FR-003**: System MUST assign a unique ID to each task
- **FR-004**: System MUST display all tasks in a numbered list format
- **FR-005**: System MUST show task status (pending/completed) for each task
- **FR-006**: System MUST allow users to mark pending tasks as complete
- **FR-007**: System MUST allow users to delete tasks by ID
- **FR-008**: System MUST allow users to update task titles
- **FR-009**: System MUST provide user-friendly error messages for invalid inputs
- **FR-010**: System MUST return to main menu after each operation
- **FR-011**: System MUST handle invalid menu selections gracefully

### Key Entities

- **Task**: Represents a single todo item
  - `id`: Unique identifier (integer, auto-incrementing)
  - `title`: Short task description (string, required)
  - `description`: Detailed task notes (string, optional, may be empty)
  - `status`: Current state (enum: "pending", "completed")
  - `created_at`: Timestamp when task was created (for ordering)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a task and see it in the list within 10 seconds of starting the application
- **SC-002**: All 5 core operations (add, list, complete, update, delete) work correctly via CLI interaction
- **SC-003**: Task list displays correctly with 10+ tasks without confusion
- **SC-004**: Invalid inputs (empty title, non-existent ID) produce clear error messages
- **SC-005**: Users can complete the happy path (add → list → complete → list) in under 2 minutes
- **SC-006**: System behavior is deterministic - same inputs always produce same outputs

## Assumptions

- Single-user application (no user accounts or authentication)
- Tasks stored in memory only (lost when application exits)
- Task IDs are 1-based integers that increment with each task
- Console is standard input/output (no colors or special formatting required)
- Menu-driven interaction (user selects options by number)
- "q" or "quit" exits the application

## Out of Scope

- Task persistence (saving to file or database)
- Multiple task lists or projects
- Task categories, tags, or priorities
- Due dates or reminders
- Search or filter functionality
- Undo or history of changes
- Export or import tasks
- User authentication or accounts
