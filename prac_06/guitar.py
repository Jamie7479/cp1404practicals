"""
Guitar Class
Estimated time: 5mins
Start time: 12.47
End time: 12.57
Duration: 10mins
"""


class Guitar:
    """Create guitar representation"""
    CURRENT_YEAR = 2025

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        return self.get_age() >= 50
