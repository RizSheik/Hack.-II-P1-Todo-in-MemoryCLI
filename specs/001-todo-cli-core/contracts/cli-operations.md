# CLI Operations Contract: todo-cli-core

**Feature**: 001-todo-cli-core | **Date**: 2025-12-30

## Main Menu

```
=======================================
          TODO APPLICATION
=======================================

1. Add task
2. List tasks
3. Complete task
4. Update task
5. Delete task
6. Exit

Enter your choice (1-6): _
```

## Operation 1: Add Task

### Input Flow

```
Enter choice: 1

=== Add New Task ===
Enter task title: Buy milk
Enter description (optional, press Enter to skip): Get 2% milk from store
```

### Success Output

```
✅ Task added successfully! (ID: 1)
```

### Error Cases

| Error | Input | Message |
|-------|-------|---------|
| Empty title | (empty) | ❌ Error: Task title cannot be empty. Please try again. |
| Whitespace only | "   " | ❌ Error: Task title cannot be empty. Please try again. |

---

## Operation 2: List Tasks

### Input Flow

```
Enter choice: 2
```

### Success Output (with tasks)

```
=== Your Tasks ===

ID | Status     | Title
--------------------
1  | [PENDING]  | Buy milk
2  | [COMPLETE] | Pay bills

Total: 2 tasks (1 pending, 1 completed)
```

### Success Output (empty list)

```
=== Your Tasks ===

No tasks yet! Add your first task.

Total: 0 tasks
```

### Error Cases

None - always succeeds

---

## Operation 3: Complete Task

### Input Flow

```
Enter choice: 3

=== Complete Task ===
Enter task ID to complete: 1
```

### Success Output

```
✅ Task #1 marked as complete!
```

### Success Output (already complete)

```
✅ Task #1 was already complete. (idempotent)

### Error Cases

| Error | Input | Message |
|-------|-------|---------|
| Invalid ID (non-numeric) | "abc" | ❌ Error: Please enter a valid number. |
| Non-existent ID | 999 | ❌ Error: Task #999 not found. |

---

## Operation 4: Update Task

### Input Flow

```
Enter choice: 4

=== Update Task ===
Enter task ID to update: 1
Enter new title: Buy oat milk
Update description? (y/n): y
Enter new description (or press Enter to keep current):
```

### Success Output

```
✅ Task #1 updated successfully!
```

### Alternative (skip description)

```
✅ Task #1 updated successfully! (description unchanged)
```

### Error Cases

| Error | Input | Message |
|-------|-------|---------|
| Invalid ID | 999 | ❌ Error: Task #999 not found. |
| Empty new title | "" | ❌ Error: Task title cannot be empty. |

---

## Operation 5: Delete Task

### Input Flow

```
Enter choice: 5

=== Delete Task ===
Enter task ID to delete: 1
```

### Confirmation Prompt

```
⚠️  Are you sure you want to delete task #1 "Buy milk"? (y/n): y
```

### Success Output

```
✅ Task #1 deleted successfully!
```

### Error Cases

| Error | Input | Message |
|-------|-------|---------|
| Invalid ID | "abc" | ❌ Error: Please enter a valid number. |
| Non-existent ID | 999 | ❌ Error: Task #999 not found. |
| Cancelled | n | Delete cancelled. Returning to menu. |

---

## Operation 6: Exit

### Input Flow

```
Enter choice: 6
```

### Output

```
👋 Thanks for using Todo! Goodbye.
```

---

## Global Error Handling

### Invalid Menu Selection

```
❌ Error: Invalid choice. Please enter a number 1-6.
```

### Keyboard Interrupt (Ctrl+C)

```
\n👋 Goodbye!
```

---

## User Experience Rules

1. After ANY operation (success or error), return to main menu
2. Error messages start with ❌ to draw attention
3. Success messages start with ✅
4. Warning messages start with ⚠️
5. All messages are on a single line (no multi-line errors)
6. Empty input handling is consistent across operations
