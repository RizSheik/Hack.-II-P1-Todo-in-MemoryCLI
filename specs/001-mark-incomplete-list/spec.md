# Feature Specification: Todo App Enhancement - Mark Task Incomplete & Improved List View

**Feature Branch**: `001-mark-incomplete-list`
**Created**: 2026-01-01
**Status**: Draft
**Input**: User description: "Enhancement Features to Specify:\n1. Mark Task Incomplete:\n   - User can toggle a completed task back to pending\n   - Input validation for task id\n   - Edge case: already pending task\n   - Update status field in Task dataclass\n\n2. Improved List View:\n   - Show tasks in tabular format\n   - Include: ID, Title, Status (PENDING/COMPLETED), Created At\n   - Highlight completed tasks visually (e.g.,  for complete,  for pending)\n   - Sort tasks by created_at by default\n   - Handle empty task list gracefully"

## User Scenarios & Testing

### User Story 1 - Mark a Completed Task as Incomplete (Priority: P1)

As a user who accidentally completed a task or wants to reopen work, I want to mark a completed task as pending again, so that I can track work that needs to be done.

**Why this priority**: This is a core undo operation that provides users flexibility to correct mistakes. Without it, users cannot recover from accidental completions, reducing trust in the application.

**Independent Test**: Can be fully tested by completing a task, then marking it incomplete, and verifying the status changes back to pending with appropriate feedback.

**Acceptance Scenarios**:

1. **Given** a task exists with COMPLETED status, **When** the user marks it incomplete, **Then** the task status changes to PENDING and the user receives a confirmation message.

2. **Given** multiple completed tasks exist, **When** the user marks one incomplete, **Then** only that specific task's status changes; other tasks remain unaffected.

3. **Given** a non-existent task ID is provided, **When** the user attempts to mark it incomplete, **Then** the system displays an error message indicating the task was not found.

---

### User Story 2 - View Tasks in Tabular Format (Priority: P1)

As a user with multiple tasks, I want to see my tasks displayed in a clean table format with clear status indicators, so that I can quickly scan and understand my task list.

**Why this priority**: The list view is the primary way users review their work. A well-formatted table improves readability and user experience significantly.

**Independent Test**: Can be fully tested by adding tasks with different statuses and verifying the list command displays them in a properly formatted table.

**Acceptance Scenarios**:

1. **Given** multiple tasks exist with various statuses, **When** the user views the task list, **Then** tasks are displayed in a tabular format with columns for ID, Title, Status, and Created At.

2. **Given** tasks exist with different creation timestamps, **When** the user views the list, **Then** tasks are sorted by creation time (oldest first) by default.

3. **Given** a task is completed, **When** displayed in the list, **Then** it shows a visual indicator (e.g., checkmark or "COMPLETE") that distinguishes it from pending tasks.

4. **Given** no tasks exist, **When** the user requests the list, **Then** a friendly message is displayed indicating the task list is empty.

---

### User Story 3 - See Task Timestamps (Priority: P2)

As a user who creates tasks over time, I want to see when each task was created, so that I can understand the chronology of my work.

**Why this priority**: Timestamps provide context about when tasks were added, helping users prioritize recent vs. older tasks.

**Independent Test**: Can be fully tested by adding tasks at different times and verifying the Created At column displays correctly formatted timestamps.

---

### User Story 4 - Clear Visual Status Indicators (Priority: P2)

As a user, I want completed tasks to be visually distinct from pending tasks, so that I can quickly identify what is done versus what remains.

**Why this priority**: Visual differentiation reduces cognitive load when scanning the task list, allowing users to focus on remaining work.

**Independent Test**: Can be fully tested by creating mixed status tasks and verifying the display uses consistent visual markers for each status.

---

### Edge Cases

- **Already pending task**: When a user attempts to mark a task incomplete that is already pending, the system should provide feedback that no change was made.
- **Invalid input**: Non-numeric task ID input should be rejected with a clear error message.
- **Concurrent modifications**: (Not applicable for single-user CLI with in-memory storage)
- **Long task titles**: The tabular display should handle titles of varying lengths gracefully without breaking the table layout.
- **Empty task list**: The list view should handle the empty state with a user-friendly message.

## Requirements

### Functional Requirements

- **FR-001**: System MUST allow users to mark a task with COMPLETED status as PENDING (incomplete).
- **FR-002**: System MUST validate that the provided task ID exists before attempting to change status.
- **FR-003**: System MUST reject non-numeric task ID input with an appropriate error message.
- **FR-004**: System MUST provide user feedback upon successful status change from COMPLETED to PENDING.
- **FR-005**: System MUST display an informational message (not an error) when attempting to mark an already-pending task as incomplete, indicating no change was made.
- **FR-006**: System MUST display tasks in a tabular format with columns: ID, Title, Status, Created At.
- **FR-007**: System MUST sort tasks by creation timestamp in ascending order (oldest first) by default.
- **FR-008**: System MUST visually distinguish completed tasks from pending tasks in the list view.
- **FR-009**: System MUST display a friendly message when the task list is empty.
- **FR-010**: System MUST format Created At timestamps in a human-readable format (e.g., "YYYY-MM-DD HH:MM").

### Key Entities

- **Task**: Represents a todo item with the following attributes:
  - `id`: Unique identifier for the task (integer)
  - `title`: The task description (string)
  - `description`: Optional detailed description (string)
  - `status`: Current state - PENDING or COMPLETED (enum)
  - `created_at`: Timestamp when the task was created (datetime)

- **Status Enum**: Defines possible task states:
  - `PENDING`: Task is not yet completed
  - `COMPLETED`: Task has been finished

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can successfully mark a completed task as incomplete with a single command (100% success rate for valid inputs).
- **SC-002**: All task list displays render in a properly aligned tabular format regardless of task title length.
- **SC-003**: Users can clearly distinguish completed from pending tasks through visual indicators in the list view.
- **SC-004**: Empty task list state provides a clear, user-friendly message with no errors.
- **SC-005**: Task timestamps are displayed in a format that users can easily understand (e.g., "2026-01-01 14:30").

## Assumptions

- The application remains a single-user CLI with in-memory storage (Phase I constraints).
- Timestamps are stored in UTC and displayed in local time or as ISO format for simplicity.
- The tabular format uses fixed-width columns to handle varying content lengths.
- Visual indicators use ASCII/Unicode characters (checkmarks, brackets) compatible with standard console output.
- No persistence layer changes are required; the Task dataclass already includes created_at field.

## Out of Scope

- Bulk operations for marking multiple tasks incomplete at once.
- Filtering or sorting options beyond the default (sort by created_at).
- Color-coded output (cross-platform console color support varies).
- Pagination for large task lists (not expected in CLI context).
- Export functionality for task data.

## Dependencies

- Existing Task dataclass with id, title, description, status, and created_at fields.
- Existing in-memory task storage (list of Task objects).
- Existing Status enumeration (PENDING, COMPLETED).
- Existing get_next_id() function for task ID generation.
