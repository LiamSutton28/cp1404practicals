"""Taxi Simulator program"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    """User interface for taxis"""
    current_taxi = None
    total_fare = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis()
            current_taxi = change_taxi()
        elif choice == "d":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                drive_taxi(current_taxi)
                total_fare += current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():,.2f}")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare:,.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    display_farewell_summary(total_fare)


def display_farewell_summary(total_fare: int):
    """Display farewell summary of all taxis."""
    print(f"Total trip cost: ${total_fare:,.2f}")
    print(f"Taxis are now:")
    display_taxis()


def drive_taxi(current_taxi: Taxi | SilverServiceTaxi):
    """Drive current taxi the unput distance."""
    distance = int(input("Drive how far? "))
    current_taxi.start_fare()
    current_taxi.drive(distance)


def change_taxi():
    """Change current taxi if valid."""
    try:
        taxi_index = int(input("Choose taxi: "))
        return taxis[taxi_index]
    except IndexError:
        print("Invalid taxi choice")


def display_taxis():
    """Display all the Taxis."""
    for i, car in enumerate(taxis):
        print(f"{i} - {car}")


main()