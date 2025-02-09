import pytest
from projects import Project

def test_project():
    project = Project("Test project")
    assert repr(project) == "Project(Test project, [], 0, 0)"

