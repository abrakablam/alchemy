import pytest
from projects import Project
from tasks import Task

def test_project():
    project = Project("Test project")
    assert repr(project) == "Project(Test project, [], 0, 0)"

def test_add_task():
    project = Project("Test project")
    project.tasks(Task("Test task", 60))
    assert repr(project) == "Project(Test project, [Task(Test task, 60, )], 0, 0)"

def test_delete_task():
    project = Project("Test project")
    project.tasks(Task("Test task", 60))
    
