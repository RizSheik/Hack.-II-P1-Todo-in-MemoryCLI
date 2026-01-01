# Research Notes: Mark Task Incomplete & Improved List View

**Feature**: 001-mark-incomplete-list
**Date**: 2026-01-01

## Technical Decisions Resolved

### Decision 1: CLI Menu Option Placement

**Question**: Where should "Mark Incomplete" appear in the menu?

**Analysis**:
- Current menu has options 1-6: Add, List, Complete, Update, Delete, Exit
- Natural placement is option 7 (after "Complete task")
- Alternative: Submenu under "Complete" or command-line argument

**Decision**: Add as menu option 7

**Rationale**:
- Maintains single-level menu simplicity
- Mirrors "Complete" operation (opposite action)
- Easy for users to find (Complete → Uncomplete)
- Follows existing UX patterns

---

### Decision 2: Timestamp Display Format

**Question**: What format should `created_at` display in?

**Options**:
1. `YYYY-MM-DD HH:MM` (e.g., "2026-01-01 14:30")
2. `YYYY-MM-DD HH:MM:SS` (with seconds)
3. Relative time (e.g., "2 hours ago")
4. Full datetime with timezone

**Decision**: `YYYY-MM-DD HH:MM`

**Rationale**:
- Human-readable without being verbose
- ISO-like format is familiar
- Seconds unnecessary for task management
- No timezone complexity needed (single user, local display)
- Simple to implement with `datetime.strftime()`

---

### Decision 3: Visual Status Indicators

**Question**: How to visually distinguish completed vs. pending tasks?

**Options**:
1. `[X]` / `[ ]` (ASCII brackets)
2. Unicode: `[✅]` / `[❌]`
3. Text: "[COMPLETE]" / "[PENDING]"
4. Color (ANSI codes)

**Decision**: `[X]` / `[ ]` (ASCII brackets)

**Rationale**:
- Universally compatible with all terminals
- No encoding issues on Windows cmd/PowerShell
- Clean, minimal visual noise
- Already used in existing `list_tasks()` function (see line 76)
- Spec example uses this format

---

### Decision 4: Tabular Column Layout Strategy

**Question**: How to handle variable-length task titles in table display?

**Options**:
1. Fixed-width columns with truncation
2. Dynamic column widths (terminal-dependent)
3. Wrap long titles across lines
4. Just title without columns

**Decision**: Fixed-width columns with truncation

**Rationale**:
- Consistent output across terminals
- Truncation prevents broken table layout
- Simple to implement
- Matches existing code style (see line 69-70)

**Column Widths**:
- ID: 3 chars (right-aligned)
- Created: 11 chars (YYYY-MM-DD)
- Status: 7 chars (`[X]` or `[ ]`)
- Title: Remainder (truncated with `...` if > 30 chars)

---

### Decision 5: Sorting Strategy

**Question**: Should tasks be sorted, and by what?

**Analysis**:
- Spec FR-007: "sort tasks by creation timestamp in ascending order"
- Ascending = oldest first
- Python: `tasks.sort(key=lambda t: t.created_at)`

**Decision**: Sort by `created_at` ascending (oldest first)

**Rationale**:
- Matches spec requirement explicitly
- Natural chronological order
- Users can see task history at a glance
- Simple one-line sort operation

---

### Decision 6: Error Message Strategy

**Question**: How to handle different error conditions?

**Conditions**:
1. Invalid input (non-numeric)
2. Task not found
3. Task already incomplete

**Decision**:
- Invalid input: "Error: Please enter a valid number."
- Not found: "Error: Task #X not found."
- Already incomplete: "Task #X is already incomplete." (informational, not error)

**Rationale**:
- Clear, actionable messages
- Error prefix for actionable errors
- No prefix for informational messages (per FR-005)
- Consistent with existing error style (see `todo.py` lines 91, 100, 108)

---

## Code Patterns from Existing Codebase

### Existing Error Handling Pattern
```python
try:
    task_id = int(input("Enter task ID: "))
except ValueError:
    print("Error: Please enter a valid number.")
    return
```

### Existing Task Lookup Pattern
```python
for task in tasks:
    if task.id == task_id:
        # found
        return
print(f"Error: Task #{task_id} not found.")
```

### Existing Status Display Pattern
```python
status_str = "[COMPLETE]" if task.status == Status.COMPLETED else "[PENDING]"
```

---

## References

- Existing `todo.py` implementation (lines 1-188)
- Python `datetime.strftime()` format codes
- Python list sorting: `list.sort(key=...)`
