"""
Programming Language Class
Estimated time: 15mins
Start time: 12.32
End time: 12.40
Duration: 8mins
"""


class ProgrammingLanguage:
    """Represent Programming Language instance"""

    def __init__(self, name, typing, reflection, year):
        """Initialise programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string summary"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determines if language instance is dynamic"""
        return self.typing == "Dynamic"
