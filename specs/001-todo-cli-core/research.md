# Research: todo-cli-core

**Feature**: 001-todo-cli-core | **Date**: 2025-12-30

## Decision: Python Version

**Decision**: Python 3.8+

**Rationale**:
- Python 3.8 is the minimum version that supports all required features
- f-strings (Python 3.6+) for clean string formatting
- dataclasses (Python 3.7+) for simple Task class definition
- Widely available on all major platforms
- Compatible with most CI/CD environments

**Alternatives Considered**:
- Python 3.11+: Newer features available, but less universally installed
- Python 3.6: Would require .format() instead of f-strings (minor)

## Decision: No External Dependencies

**Decision**: Standard library only

**Rationale**:
- Constitution requirement: "No external dependencies"
- Simplifies installation: `python todo.py` works anywhere
- No version conflicts or dependency management
- Easier for judges to review code

**Standard Library Modules Used**:
- `sys` - for stdin/stdout and exit handling
- `datetime` - for task timestamp
- `enum` - for Status enum

**Alternatives Considered**:
- colorama: ANSI colors (rejected - adds complexity)
- click/argparse: CLI frameworks (rejected - standard input() sufficient)
- pytest: Dev dependency only (not bundled)

## Decision: In-Memory Storage

**Decision**: Python list of Task objects

**Rationale**:
- Constitution requirement: "In-memory data storage"
- Simplest data structure for ordered list
- O(1) append, O(n) search (acceptable for <1000 tasks)
- Natural iteration order (creation order preserved)

**Alternatives Considered**:
- Dictionary: O(1) lookup but no natural order, harder for list display
- deque: Slightly faster but list is simpler and sufficient

## Decision: Menu-Driven CLI

**Decision**: Numbered menu with standard input()

**Rationale**:
- Most intuitive for non-technical users
- Clear flow: see options → choose → do action → return to menu
- Easy to validate input (integer 1-6)
- Works in any terminal without special capabilities

**Menu Structure**:
```
1. Add task
2. List tasks
3. Complete task
4. Update task
5. Delete task
6. Exit
```

**Alternatives Considered**:
- Command-line arguments (todo add "task"): Harder to remember syntax
- REPL mode (todo> add): More complex implementation
- Single-key shortcuts (a=add, l=list): Less discoverable

## Decision: Task ID System

**Decision**: 1-based integer, auto-incrementing

**Rationale**:
- User-friendly: "Complete task 3" is intuitive
- Simple implementation: len(tasks) + 1 or max ID + 1
- Handles gaps from deletion: gaps are acceptable, IDs never reused

**Alternatives Considered**:
- 0-based: Less intuitive for users
- UUID: Overkill, harder to type/reference
- Reuse IDs after deletion: Adds complexity, no user benefit

## Decision: Single File Structure

**Decision**: todo.py as single entry point

**Rationale**:
- Maximum simplicity for Phase I
- All code visible in one file
- Easy to run: `python todo.py`
- Beginner-friendly structure

**Alternatives Considered**:
- Separate files (task.py, cli.py, etc.): Unnecessary abstraction for 5 operations
- Package structure: Over-engineering for single-user CLI

## Best Practices Reference

### Python CLI Patterns
- Use `if __name__ == "__main__":` guard
- Wrap main loop in try-except for graceful error handling
- Use `sys.exit()` for clean exits
- Keep functions under 50 lines when possible

### Error Handling
- Catch `KeyboardInterrupt` (Ctrl+C) gracefully
- Validate input before processing
- Provide clear, user-friendly error messages
- Always return to main menu after errors

### Code Organization
- Main menu loop
- Separate functions for each operation
- Task class/dataclass for entity
- No global state beyond task list
