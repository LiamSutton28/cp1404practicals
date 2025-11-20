"""Test code for SilverService object"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

normal_taxi = Taxi("Ranger", 100)
pricey_taxi = SilverServiceTaxi("Lamborghini", 100, 2)
test_taxi = SilverServiceTaxi("Lamborghini", 100, 2)
normal_taxi.drive(100)
pricey_taxi.drive(100)
test_taxi.drive(18)
print(normal_taxi.get_fare())
print(f"{pricey_taxi.get_fare()} should be equal to {normal_taxi.get_fare() * 2 + 4.5}")
print(test_taxi.get_fare())