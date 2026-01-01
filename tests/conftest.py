"""Pytest configuration and fixtures for todo tests."""

import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from todo import Task, Status, tasks, get_next_id


@pytest.fixture(autouse=True)
def clean_tasks():
    """Clean task list before each test."""
    tasks.clear()
    yield
    tasks.clear()
