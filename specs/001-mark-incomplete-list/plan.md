# Implementation Plan: Mark Task Incomplete & Improved List View

**Branch**: `001-mark-incomplete-list` | **Date**: 2026-01-01 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification for two enhancements - Mark Task Incomplete and Improved List View

## Summary

Implement two CLI enhancements for the Todo App:
1. **Mark Task Incomplete** (T025-T026): New menu option to toggle completed tasks back to pending with input validation
2. **Improved List View** (T027-T028): Enhanced tabular display with ID, Title, Status, Created At columns; visual status indicators; sorted by created_at

Both features leverage existing Task dataclass and in-memory storage. No external dependencies required.

## Technical Context

**Language/Version**: Python 3.x (existing codebase uses type hints, no version specified)
**Primary Dependencies**: None (standard library only, per Phase I constraints)
**Storage**: In-memory list (existing `tasks: list[Task]`)
**Testing**: Manual CLI verification (existing pattern in project)
**Target Platform**: Console/CLI (Windows, macOS, Linux)
**Project Type**: Single-file Python CLI application (`todo.py`)
**Performance Goals**: Instant response (single-user, in-memory operations)
**Constraints**: Phase I constraints apply - no database, no external services, synchronous execution
**Scale/Scope**: Single user, <100 tasks expected in typical usage

## Constitution Check

*GATE: Must pass before proceeding. Re-check after Phase 1 design.*

| Check | Status | Notes |
|-------|--------|-------|
| Python only | ✅ PASS | Existing `todo.py` is Python |
| CLI interface | ✅ PASS | Console-based menu system |
| In-memory storage | ✅ PASS | Uses `tasks: list[Task]` |
| Single-user | ✅ PASS | No session management needed |
| Synchronous | ✅ PASS | All operations are blocking |
| No external dependencies | ✅ PASS | Only standard library (`datetime`, `enum`, `sys`) |
| Traceable to spec | ✅ PASS | Each task maps to FR-001 through FR-010 |
| Educational readability | ✅ PASS | Simple loops and conditionals preferred |
| Error handling required | ✅ PASS | Invalid IDs, empty inputs handled |

## Project Structure

### Documentation (this feature)

```text
specs/001-mark-incomplete-list/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification (/sp.specify output)
├── research.md          # Technical decisions (created below)
├── data-model.md        # Entity definitions (created below)
└── checklists/
    └── requirements.md  # Quality validation
```

### Source Code (repository root)

```text
todo.py                 # Single-file application (MODIFIED)
```

**Structure Decision**: Single-file Python CLI application at repository root. All modifications will be made to `todo.py`.

## Technical Design Decisions

### Decision 1: CLI Menu Option for "Mark Incomplete"

**Choice**: Add menu option 7 "Mark task incomplete"

**Rationale**: Follows existing menu pattern (options 1-6 currently exist). New option fits logically after "Complete task" (option 3).

**Alternative Considered**: Submenu or command-line argument (e.g., `python todo.py --uncomplete 1`)
- Rejected: Submenu adds complexity; CLI args not part of current UX pattern

### Decision 2: Timestamp Format for Display

**Choice**: `YYYY-MM-DD HH:MM` format (e.g., "2026-01-01 14:30")

**Rationale**: Human-readable, compact, follows ISO-like convention. Uses Python's `strftime("%Y-%m-%d %H:%M")`.

**Alternative Considered**: Full datetime with seconds
- Rejected: Seconds unnecessary for task management; adds visual noise

### Decision 3: Visual Status Indicators

**Choice**: `[X]` for COMPLETED, `[ ]` for PENDING

**Rationale**: Clear visual distinction using ASCII characters. Compatible with all terminals. Consistent with spec's example.

**Alternative Considered**: Unicode checkmarks (✅/❌)
- Rejected: Terminal encoding issues on some Windows configurations; `[X]`/`[ ]` is universally safe

### Decision 4: Tabular Column Layout

**Choice**: Fixed-width columns with dynamic title truncation

```
 ID | Created     | Status | Title
----+-------------+--------+--------------------------
  1 | 2026-01-01  | [X]    | Buy groceries
  2 | 2026-01-01  | [ ]    | Finish report
```

**Rationale**: Fixed widths handle varying title lengths gracefully. Column headers explain content.

**Column Specs**:
- ID: 3 chars right-aligned
- Created: 11 chars (YYYY-MM-DD)
- Status: 7 chars (`[X]` or `[ ]` + padding)
- Title: Remaining space, truncated with `...` if needed

### Decision 5: Sorting Behavior

**Choice**: Sort by `created_at` ascending (oldest first)

**Rationale**: Natural chronological order. Users see task creation history. Matches spec FR-007.

**Alternative Considered**: Sort by status then creation
- Rejected: Spec explicitly requires sort by created_at

## Implementation Tasks

### T025: Add "Mark Incomplete" Menu Option

**Reference**: FR-001, FR-002, FR-003, FR-004, FR-005

**Actions**:
1. Add menu option "7. Mark task incomplete" to `show_menu()`
2. Create `uncomplete_task()` function
3. Implement input validation for numeric task ID
4. Add error handling for non-existent task ID
5. Handle already-pending task edge case

**CLI Flow**:
```
7. Mark task incomplete
Enter task ID to mark incomplete: [user input]
```
- Success: "Task #X marked as incomplete!"
- Not found: "Error: Task #X not found."
- Already pending: "Task #X is already incomplete."
- Invalid input: "Error: Please enter a valid number."

### T026: Implement Uncomplete Task Function

**Reference**: FR-001, FR-004, FR-005

**Function Signature**:
```python
def uncomplete_task():
    """Mark a completed task as incomplete (pending)."""
    try:
        task_id = int(input("Enter task ID to mark incomplete: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    for task in tasks:
        if task.id == task_id:
            if task.status == Status.COMPLETED:
                task.status = Status.PENDING
                print(f"Task #{task_id} marked as incomplete!")
            else:
                print(f"Task #{task_id} is already incomplete.")
            return

    print(f"Error: Task #{task_id} not found.")
```

### T027: Enhance List View with Tabular Format

**Reference**: FR-006, FR-007, FR-008, FR-010

**Actions**:
1. Modify `list_tasks()` function
2. Add timestamp formatting
3. Implement sorting by `created_at`
4. Create tabular column layout
5. Add visual status indicators `[X]`/`[ ]`

**Print Layout**:
```python
# Column widths
ID_WIDTH = 3
DATE_WIDTH = 11
STATUS_WIDTH = 7

# Header
print(f" ID | Created     | Status | Title")
print("-" * 50)

# Row example
print(f" 1  | 2026-01-01  | [X]    | Buy groceries")
```

### T028: Handle Edge Cases in List View

**Reference**: FR-009, Edge Cases

**Actions**:
1. Ensure empty list message (existing, verify friendly wording)
2. Handle long titles with truncation
3. Verify status indicator consistency

**Empty List Message** (verify/update):
"=== Your Tasks ===" followed by "No tasks yet! Add your first task."

**Long Title Handling**:
```python
MAX_TITLE_WIDTH = 30
if len(task.title) > MAX_TITLE_WIDTH:
    display_title = task.title[:MAX_TITLE_WIDTH-3] + "..."
else:
    display_title = task.title
```

## Complexity Tracking

> No Constitution violations to justify. All requirements satisfy Phase I constraints.

## Phase 1 Artifacts

The following artifacts are generated by `/sp.plan`:

| File | Purpose |
|------|---------|
| `research.md` | Technical decisions documented above |
| `data-model.md` | Entity definitions (Task, Status) |

## Next Steps

After `/sp.plan` approval:
1. Run `/sp.tasks` to generate task breakdown
2. Each task (T025-T028) will have acceptance criteria
3. Implement in order T025 → T026 → T027 → T028
4. Test each feature independently before combining
