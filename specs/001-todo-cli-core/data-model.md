# Data Model: todo-cli-core

**Feature**: 001-todo-cli-core | **Date**: 2025-12-30

## Task Entity

### Attributes

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `id` | int | Yes | Auto-increment | Unique identifier (1-based) |
| `title` | str | Yes | N/A | Short task description |
| `description` | str | No | "" | Detailed task notes |
| `status` | Status | Yes | Status.PENDING | Current state |
| `created_at` | datetime | Yes | Auto-generate | Creation timestamp |

### Status Enum

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
```

### Validation Rules

| Rule | Implementation |
|------|----------------|
| Title required | `if not title or not title.strip(): raise ValueError` |
| Title not whitespace-only | `if not title.strip(): raise ValueError` |
| Description optional | Default empty string "" |
| ID assigned by system | Never user-provided |

## State Transitions

### Task Lifecycle

```
CREATED → PENDING → COMPLETED
              ↓
           DELETED (removed from list)
```

### Valid Transitions

| From State | To State | Action | Allowed? |
|------------|----------|--------|----------|
| (new) | PENDING | add_task() | ✅ Yes |
| PENDING | COMPLETED | complete_task() | ✅ Yes |
| PENDING | DELETED | delete_task() | ✅ Yes |
| COMPLETED | COMPLETED | complete_task() | ✅ Yes (idempotent) |
| COMPLETED | DELETED | delete_task() | ✅ Yes |
| DELETED | N/A | Any action | ❌ No (task gone) |

### Invalid Transition Handling

| Attempted Action | Error Message | Behavior |
|------------------|---------------|----------|
| Complete deleted task | "Task not found" | Error, return to menu |
| Update deleted task | "Task not found" | Error, return to menu |
| Delete deleted task | "Task not found" | Error, return to menu |

## In-Memory Storage Model

### Data Structure

```python
tasks: list[Task] = []  # Global task list
next_id: int = 1  # Auto-increment counter
```

### Properties

| Property | Value |
|----------|-------|
| Order | FIFO (creation order) |
| Access | Sequential (list iteration) |
| Search | Linear (O(n)) |
| Modification | Mutable (append, remove, update) |

### ID Assignment Logic

```python
def get_next_id() -> int:
    """Get next available task ID."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1
```

**Note**: IDs are never reused, even after deletion.

## Example Data

```
tasks = [
    Task(
        id=1,
        title="Buy milk",
        description="Get 2% milk from store",
        status=Status.PENDING,
        created_at=datetime(2025, 12, 30, 10, 0, 0)
    ),
    Task(
        id=2,
        title="Pay bills",
        description="Electric and internet",
        status=Status.COMPLETED,
        created_at=datetime(2025, 12, 30, 9, 0, 0)
    )
]
```
