"""Unit tests for Task class and related functions."""

import pytest
from datetime import datetime
from unittest.mock import patch
from todo import Task, Status, get_next_id, tasks, uncomplete_task


class TestTask:
    """Tests for Task class initialization."""

    def test_task_creation_defaults(self):
        """Test task with default values."""
        task = Task(id=1, title="Test task")
        assert task.id == 1
        assert task.title == "Test task"
        assert task.description == ""
        assert task.status == Status.PENDING
        assert isinstance(task.created_at, datetime)

    def test_task_creation_with_all_params(self):
        """Test task with all parameters."""
        task = Task(id=1, title="Test", description="Details", status=Status.COMPLETED)
        assert task.id == 1
        assert task.title == "Test"
        assert task.description == "Details"
        assert task.status == Status.COMPLETED


class TestGetNextId:
    """Tests for get_next_id function."""

    def test_first_task_id(self, clean_tasks):
        """Test ID for first task."""
        assert get_next_id() == 1

    def test_incrementing_ids(self, clean_tasks):
        """Test ID increments correctly."""
        tasks.append(Task(id=1, title="Task 1"))
        assert get_next_id() == 2

        tasks.append(Task(id=2, title="Task 2"))
        assert get_next_id() == 3

    def test_id_after_deletion(self, clean_tasks):
        """Test IDs are not reused after deletion."""
        tasks.append(Task(id=1, title="Task 1"))
        tasks.append(Task(id=2, title="Task 2"))
        tasks.pop(0)  # Delete first task
        assert get_next_id() == 3  # Should still be 3, not 1


class TestUncompleteTask:
    """Tests for uncomplete_task function."""

    def test_uncomplete_completed_task(self, clean_tasks, capsys):
        """Test marking a completed task as incomplete."""
        task = Task(id=1, title="Test task", status=Status.COMPLETED)
        tasks.append(task)

        with patch('builtins.input', return_value='1'):
            uncomplete_task()

        assert task.status == Status.PENDING
        captured = capsys.readouterr()
        assert "marked as incomplete" in captured.out

    def test_uncomplete_already_pending_task(self, clean_tasks, capsys):
        """Test marking an already pending task as incomplete."""
        task = Task(id=1, title="Test task", status=Status.PENDING)
        tasks.append(task)

        with patch('builtins.input', return_value='1'):
            uncomplete_task()

        assert task.status == Status.PENDING
        captured = capsys.readouterr()
        assert "already incomplete" in captured.out

    def test_uncomplete_nonexistent_task(self, clean_tasks, capsys):
        """Test marking a non-existent task as incomplete."""
        with patch('builtins.input', return_value='999'):
            uncomplete_task()

        captured = capsys.readouterr()
        assert "not found" in captured.out

    def test_uncomplete_invalid_input(self, clean_tasks, capsys):
        """Test invalid input for uncomplete task."""
        with patch('builtins.input', return_value='abc'):
            uncomplete_task()

        captured = capsys.readouterr()
        assert "valid number" in captured.out


class TestListTasks:
    """Tests for list_tasks function."""

    def test_list_tasks_sorting(self, clean_tasks):
        """Test that tasks are sorted by created_at."""
        from datetime import datetime, timedelta

        # Create tasks with different timestamps
        task1 = Task(id=1, title="Task 1")
        task1.created_at = datetime.now() - timedelta(hours=1)

        task2 = Task(id=2, title="Task 2")
        task2.created_at = datetime.now()

        task3 = Task(id=3, title="Task 3")
        task3.created_at = datetime.now() - timedelta(hours=2)

        tasks.extend([task1, task2, task3])

        # Import list_tasks and capture output
        from todo import list_tasks
        from unittest.mock import patch
        import io
        import sys

        captured = io.StringIO()
        with patch('sys.stdout', captured):
            list_tasks()

        output = captured.getvalue()
        # Task 3 should appear first (oldest), then task 1, then task 2 (newest)
        # Filter lines that contain just task titles (not header)
        lines = [l for l in output.split('\n') if 'Task 1' in l or 'Task 2' in l or 'Task 3' in l]
        # First line should be Task 3 (oldest), last should be Task 2 (newest)
        assert "Task 3" in lines[0], f"Expected Task 3 first, got: {lines}"
        assert "Task 2" in lines[-1], f"Expected Task 2 last, got: {lines}"

    def test_list_tasks_status_indicators(self, clean_tasks, capsys):
        """Test that status indicators are displayed correctly."""
        from unittest.mock import patch

        task1 = Task(id=1, title="Completed task", status=Status.COMPLETED)
        task2 = Task(id=2, title="Pending task", status=Status.PENDING)
        tasks.extend([task1, task2])

        with patch('builtins.input', side_effect=['1', '2']):
            from todo import list_tasks
            list_tasks()

        captured = capsys.readouterr()
        output = captured.out
        assert "[X]" in output
        assert "[ ]" in output

    def test_list_tasks_empty(self, clean_tasks, capsys):
        """Test empty task list message."""
        from unittest.mock import patch
        from todo import list_tasks

        with patch('builtins.input', side_effect=['1', '2']):
            list_tasks()

        captured = capsys.readouterr()
        assert "No tasks yet" in captured.out

