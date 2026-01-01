# Quickstart: todo-cli-core

**Feature**: 001-todo-cli-core | **Date**: 2025-12-30

## Running the Application

```bash
python todo.py
```

Or on Windows:

```powershell
python todo.py
```

## Quick Tour (2 minutes)

### Step 1: Add Your First Task

```
Enter your choice (1-6): 1

=== Add New Task ===
Enter task title: Buy milk
Enter description (optional, press Enter to skip): Get 2% milk

✅ Task added successfully! (ID: 1)
```

### Step 2: Add More Tasks

```
Enter your choice (1-6): 1

=== Add New Task ===
Enter task title: Pay bills
Enter description (optional, press Enter to skip):

✅ Task added successfully! (ID: 2)
```

### Step 3: View Your Tasks

```
Enter your choice (1-6): 2

=== Your Tasks ===

ID | Status     | Title
--------------------
1  | [PENDING]  | Buy milk
2  | [PENDING]  | Pay bills

Total: 2 tasks (2 pending)
```

### Step 4: Complete a Task

```
Enter your choice (1-6): 3

=== Complete Task ===
Enter task ID to complete: 1

✅ Task #1 marked as complete!
```

### Step 5: See Progress

```
Enter your choice (1-6): 2

=== Your Tasks ===

ID | Status     | Title
--------------------
1  | [COMPLETE] | Buy milk
2  | [PENDING]  | Pay bills

Total: 2 tasks (1 pending, 1 completed)
```

### Step 6: Exit

```
Enter your choice (1-6): 6

👋 Thanks for using Todo! Goodbye.
```

## Menu Reference

| Option | Action | Quick Key |
|--------|--------|-----------|
| 1 | Add a new task | a |
| 2 | View all tasks | l |
| 3 | Mark task complete | c |
| 4 | Edit task title | u |
| 5 | Remove a task | d |
| 6 | Close application | x, q |

*Note: Menu accepts full number (1-6) or first letter*

## Common Questions

**Q: How do I add a description?**
A: After entering the title, press Enter to skip, or type a description.

**Q: Can I have duplicate task titles?**
A: Yes! This version allows duplicates. Use task ID to distinguish.

**Q: What happens if I close the app?**
A: Tasks are stored in memory only. They will be lost when you exit.

**Q: How do I correct a typo in a task title?**
A: Use option 4 (Update) to edit the title.

**Q: Can I undo a deletion?**
A: No. Deleted tasks are permanently removed. Consider completing instead.
