from typing import List

class Project:
    def __init__(self, name) -> None:
        self.name = name
        self._tasks = []
        self._total_time = 0 # this will need to be updated as tasks tick upwards in time tracked
        self._estimated_time = 0 # this will need to be updated when a new task is added

    def __repr__(self) -> str:
        return f"Project({self.name}, {self._tasks}, {self._total_time}, {self._estimated_time})"

    # can't seem to use these setters and getters with @property, tests fail.
    def get_tasks(self) -> List:
        return self._tasks

    def tasks(self, task) -> None:
        self._tasks.append(task)

    def del_task(self, task_name):
        for task in self._tasks:
            if task.name == task_name:
                print(f"Task name: {task.name}")
            else:
                print("not in array")

    def get_total_time(self) -> int:
        return self._total_time



