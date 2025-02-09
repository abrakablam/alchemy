from tasks import Task
import pytest

def test_task_obj():
    task = Task("testing", 60, "test description")
    assert repr(task) == "Task(testing, 60, test description)"

def test_get_time():
    task = Task("testing", 60, "test description")
    assert task.estimated_time == 60

def test_updating_time():
    task = Task("testing", 60, "test description")
    task.total_time = 60
    assert task.total_time == 60

def test_time_typing():
    task = Task("testing", 60, "test description")
    with pytest.raises(ValueError):
        task.total_time = "60"

def test_estimated_time():
    task = Task("testing", 60, "test description")
    assert task.estimated_time == 60

def test_set_estimated_time():
    task = Task("testing", 60, "test description")
    with pytest.raises(ValueError):
        task.estimated_time = "60"
