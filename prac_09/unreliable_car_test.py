"""Test the unreliable car object"""
from prac_09.unreliable_car import UnreliableCar

bad_car = UnreliableCar("Triton", 100,30)
car_drove = 0
for i in range(0, 100):
    driven_distance = bad_car.drive(1)
    if driven_distance:
        car_drove += 1
print(f"Car drove {car_drove} times")