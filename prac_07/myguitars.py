"""My Guitars program"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars()
    display_guitars(guitars)
    # sort guitars by year made
    guitars.sort()
    display_guitars(guitars)


def display_guitars(guitars: list):
    for guitar in guitars:
        print(guitar)


def load_guitars():
    """Get guitars from a csv file and put them into a list of Guitar objects"""
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
