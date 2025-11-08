"""
Define project Class
"""


class Project:
    """Create project representation"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return str(vars(self))

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100

    def is_on_or_after(self, date):
        return self.start_date >= date
