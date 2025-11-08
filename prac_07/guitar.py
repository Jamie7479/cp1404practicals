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
        """Initialise guitar fields"""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Define string representation"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Determine if self year is less than other year"""
        return self.year < other.year

    def get_age(self):
        """Return age of guitar"""
        return 2025 - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= 50


