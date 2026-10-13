from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

def test_initialises_task():
    mock_task = Mock()
    task_formatter = TaskFormatter(mock_task)
    assert task_formatter.task == mock_task

def test_format_an_incomplete_task():
     mock_task = Mock()
     mock_task.title = "Walk the dog"
     mock_task.is_complete = False
     task_formatter = TaskFormatter(mock_task)
     assert task_formatter.format() == "[ ] Walk the dog"

def test_format_a_complete_task():
     mock_task = Mock()
     mock_task.title = "Walk the dog"
     mock_task.is_complete = True
     task_formatter = TaskFormatter(mock_task)
     assert task_formatter.format() == "[X] Walk the dog"