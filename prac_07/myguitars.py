"""My Guitars program"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Execute the guitar program tasks"""
    guitars = load_guitars()
    display_guitars(guitars)
    # sort guitars by year made
    guitars.sort()
    display_guitars(guitars)
    get_new_guitar(guitars)
    save_guitars(guitars)


def save_guitars(guitars: list):
    """Writes the Guitar objects from the guitars list to the Filename."""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def get_new_guitar(guitars: list):
    """Get a new guitar from the user."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: ")[1:])
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


def display_guitars(guitars: list):
    """Print all the guitars."""
    for guitar in guitars:
        print(guitar)


def load_guitars():
    """Get guitars from a csv file and put them into a list of Guitar objects."""
    guitars = []
    with open(FILENAME, "r") as infile:
        for line in infile:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


main()
