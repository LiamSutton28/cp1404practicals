"""SilverServiceTaxi Class"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes changing fare costs."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
