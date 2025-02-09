import time

class Task:
    def __init__(self, name, estimated_time, description=""):
        self.name = name
        self.description = description
        self._created_at = time.time()
        # this will probably change based on the time tracking func
        self._total_time = 0
        self._estimated_time = estimated_time
        #TODO: add property for the parent task (how do we do that?)

    # do we need to GET the time? probably at some point.
    @property
    def total_time(self):
        return self._total_time

    @total_time.setter
    def total_time(self, new_time):
        """updates _total_time, this is measured in MM."""
        if isinstance(new_time, int):
            self._total_time += new_time
        else:
            raise ValueError("Times must be integers.")

    @total_time.deleter
    def total_time(self):
        del self._total_time

    @property
    def estimated_time(self):
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, new_estimate):
        """Sets the _estimated time. Measured in MM"""
        if isinstance(new_estimate, int):
            self._estimated_time = new_estimate
        else:
            raise ValueError("Times must be integers.")

    @estimated_time.deleter
    def estimated_time(self):
        del self._estimated_time

    def __repr__(self):
        return f"Task({self.name}, {self._estimated_time}, {self.description})"

