# Data Model: Mark Task Incomplete & Improved List View

**Feature**: 001-mark-incomplete-list
**Date**: 2026-01-01

## Entities

### Task

Represents a single todo item in the system.

**Attributes**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `int` | Yes | Unique identifier (auto-incremented) |
| `title` | `str` | Yes | Task description |
| `description` | `str` | No | Optional detailed notes |
| `status` | `Status` | Yes | Current state (PENDING or COMPLETED) |
| `created_at` | `datetime` | Yes | Timestamp when task was created |

**State Transitions**:

```
PENDING ←→ COMPLETED
    ↑
    └── uncomplete ──────
```

- `complete_task()`: PENDING → COMPLETED
- `uncomplete_task()`: COMPLETED → PENDING

**Validation Rules**:
- `id`: Must be positive integer, unique in task list
- `title`: Must be non-empty string (trimmed)
- `description`: Optional, can be empty string
- `status`: Must be valid Status enum value
- `created_at`: Automatically set on creation, never modified

---

### Status (Enum)

Defines possible task states.

| Value | Meaning |
|-------|---------|
| `PENDING` | Task is not yet completed |
| `COMPLETED` | Task has been finished |

**Usage**:
```python
if task.status == Status.COMPLETED:
    # completed task logic
elif task.status == Status.PENDING:
    # pending task logic
```

---

## Storage

### Task Storage

**Type**: In-memory list

```python
tasks: list[Task] = []
```

**Operations**:
- `tasks.append(task)` - Add new task
- `tasks.remove(task)` - Delete task
- `[t for t in tasks if t.id == x]` - Find by ID
- `tasks.sort(key=lambda t: t.created_at)` - Sort by creation

**Constraints**:
- Single-user, single-session
- Lost when application exits (no persistence)
- Maximum size limited by system memory

---

## Display Models

### Tabular Row

Represents a task formatted for list display.

| Column | Width | Content | Alignment |
|--------|-------|---------|-----------|
| ID | 3 | `task.id` | Right |
| Created | 11 | `task.created_at.strftime("%Y-%m-%d")` | Left |
| Status | 7 | `[X]` or `[ ]` | Left |
| Title | 30+ | `task.title[:27] + "..."` if long | Left |

**Example Output**:
```
 ID | Created     | Status | Title
----+-------------+--------+--------------------------
  1 | 2026-01-01  | [X]    | Buy groceries
  2 | 2026-01-01  | [ ]    | Finish report
```

---

## Input/Output Contracts

### `uncomplete_task()` Output

| Condition | Output |
|-----------|--------|
| Success | `Task #{id} marked as incomplete!` |
| Not found | `Error: Task #{id} not found.` |
| Already pending | `Task #{id} is already incomplete.` |
| Invalid input | `Error: Please enter a valid number.` |

### `list_tasks()` Output

| Condition | Output |
|-----------|--------|
| Empty list | `No tasks yet! Add your first task.` |
| With tasks | Tabular table with all tasks |
