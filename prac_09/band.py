class Band:
    def __init__(self, name=""):
        """Initialise a Band Object."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Represent Band as a string with musicians."""
        return f"{self.name} ({",".join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(self)

    def add(self, musician):
        """Add Musicians to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Represent Band Musicians playing their instruments."""
        for musician in self.musicians:
            print(musician.play())
