from unittest.mock import Mock
from lib.task_list import TaskList


def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour

def test_add_items_to_tasks_list():
    task_list = TaskList()
    task_1 = Mock()
    task_2 = Mock()
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.all() == [task_1,task_2]

def test_return_false_if_only_one_complete():
    task_list = TaskList()
    task_1 = Mock()
    task_2 = Mock()
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.complete.return_value = True
    task_1.is_complete.return_value = True
    task_2.complete.return_value = False
    task_1.is_complete.return_value = False
    assert task_list.all_complete() == False


def test_return_true_if_both_complete():
    task_list = TaskList()
    task_1 = Mock()
    task_2 = Mock()
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.complete.return_value = True
    task_1.is_complete.return_value = True
    task_2.complete.return_value = True
    task_1.is_complete.return_value = True
    assert task_list.all_complete() == True