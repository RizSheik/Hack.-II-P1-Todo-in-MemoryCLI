#!/usr/bin/env python3
"""
Todo CLI Application

A simple console-based todo list application with 5 core operations:
- Add tasks
- List tasks
- Complete tasks
- Update tasks
- Delete tasks

Run with: python todo.py
"""

import sys
from datetime import datetime
from enum import Enum


class Status(Enum):
    """Task status enumeration."""
    PENDING = "pending"
    COMPLETED = "completed"


class Task:
    """Represents a single todo item."""

    def __init__(self, id: int, title: str, description: str = "", status: Status = Status.PENDING):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()


# Global task storage (in-memory)
tasks: list[Task] = []


def get_next_id() -> int:
    """Get the next available task ID."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1


def add_task():
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return

    description = input("Enter description (optional, press Enter to skip): ").strip()

    task = Task(id=get_next_id(), title=title, description=description)
    tasks.append(task)
    print(f"Task added successfully! (ID: {task.id})")


def list_tasks():
    """Display all tasks in tabular format."""
    if not tasks:
        print("\n=== Your Tasks ===")
        print("\nNo tasks yet! Add your first task.")
        return

    # Sort tasks by creation time (oldest first)
    sorted_tasks = sorted(tasks, key=lambda t: t.created_at)

    # Column widths for tabular format
    ID_WIDTH = 3
    DATE_WIDTH = 11
    STATUS_WIDTH = 7
    TITLE_WIDTH = 30

    print("\n=== Your Tasks ===\n")

    # Print header
    print(f" {'ID':^{ID_WIDTH}} | {'Created':^{DATE_WIDTH}} | {'Status':^{STATUS_WIDTH}} | {'Title':<{TITLE_WIDTH}}")
    print("-" * (ID_WIDTH + 2 + DATE_WIDTH + 2 + STATUS_WIDTH + 2 + TITLE_WIDTH))

    pending_count = 0
    completed_count = 0

    for task in sorted_tasks:
        # Format timestamp as YYYY-MM-DD
        created_str = task.created_at.strftime("%Y-%m-%d")

        # Visual status indicator
        status_indicator = "[X]" if task.status == Status.COMPLETED else "[ ]"

        # Truncate long titles
        display_title = task.title
        if len(display_title) > TITLE_WIDTH:
            display_title = display_title[:TITLE_WIDTH - 3] + "..."

        # Print row with proper alignment
        print(f" {task.id:>{ID_WIDTH}} | {created_str:^{DATE_WIDTH}} | {status_indicator:^{STATUS_WIDTH}} | {display_title:<{TITLE_WIDTH}}")

        # Count by status
        if task.status == Status.COMPLETED:
            completed_count += 1
        else:
            pending_count += 1

    print(f"\nTotal: {len(tasks)} tasks ({pending_count} pending, {completed_count} completed)")


def complete_task():
    """Mark a task as complete."""
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    for task in tasks:
        if task.id == task_id:
            task.status = Status.COMPLETED
            print(f"Task #{task_id} marked as complete!")
            return

    print(f"Error: Task #{task_id} not found.")


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


def update_task():
    """Update a task's title."""
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    for task in tasks:
        if task.id == task_id:
            new_title = input("Enter new title: ").strip()
            if not new_title:
                print("Error: Task title cannot be empty.")
                return
            task.title = new_title
            print(f"Task #{task_id} updated successfully!")
            return

    print(f"Error: Task #{task_id} not found.")


def delete_task():
    """Delete a task."""
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    for task in tasks:
        if task.id == task_id:
            confirm = input(f"Delete task #{task_id} '{task.title}'? (y/n): ").lower()
            if confirm != 'y':
                print("Delete cancelled.")
                return
            tasks.remove(task)
            print(f"Task #{task_id} deleted successfully!")
            return

    print(f"Error: Task #{task_id} not found.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("          TODO APPLICATION")
    print("=" * 40)
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Mark task incomplete")
    print("7. Exit")
    print("-" * 40)


def main():
    """Main application loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            uncomplete_task()
        elif choice in ("7", "q", "quit", "exit"):
            print("\nThanks for using Todo! Goodbye.")
            break
        else:
            print("Error: Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)
