"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180,"car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # 1.
    limo = Car(100, "Limo")
    # 2.
    limo.add_fuel(20)
    # 3.
    print(limo.fuel)
    # 4.
    limo.drive(115)
    # 5.
    print(limo)


main()
