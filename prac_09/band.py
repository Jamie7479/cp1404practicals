"""Band Class for Prac 9"""


class Band():
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band instance with name and empty musician list"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band"""
        return f"{self.name} {', '.join((str(musician) for musician in self.musicians))}"

    def add(self, musician):
        """Add new musician to the band"""
        self.musicians.append(musician)

    def play(self):
        """Return a multiline string showing the instrument (or no instrument) of each musician"""
        return "\n".join((musician.play() for musician in self.musicians))
