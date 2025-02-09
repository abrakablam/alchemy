from typing import List
from tasks import Task

# Okay, so what does a project look like?
# It should contain some number of tasks
# as well as some information about the project istelf
# the total time spent across all tasks
#
# projects have no tasks when created, but they can be added later.
# each project has an array (?) of Task objects that are created with the Project name as a param
class Project:
    def __init__(self, name) -> None:
        self.name = name
        self._tasks = []
        self._total_time = 0 # this will need to be updated as tasks tick upwards in time tracked
        self._estimated_time = 0 # this will need to be updated when a new task is added

    def __repr__(self) -> str:
        return f"Project({self.name}, {self._tasks}, {self._total_time}, {self._estimated_time})"

    @property
    def tasks(self) -> List:
        return self._tasks

    @tasks.setter
    def tasks(self, task_name, estimated_time) -> None:
        new_task = Task(task_name, estimated_time, project=self.name)
        self._tasks.append(new_task)
        
        
