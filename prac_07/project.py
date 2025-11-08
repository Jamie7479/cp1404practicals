"""
Define project Class
"""


class Project:
    """Create project representation"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return object representation"""
        start_date_string = self.start_date.strftime('%d/%m/%Y')
        return f"{self.name}, start: {start_date_string}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Determine if self priority is less than other priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if project is complete"""
        return self.completion_percentage == 100

    def is_on_or_after(self, date):
        """Determine if project start date is on or after a date"""
        return self.start_date >= date
