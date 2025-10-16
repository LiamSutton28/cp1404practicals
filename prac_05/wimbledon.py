"""
Wimbledon
Estimate: 50 minutes
Actual:   todo minutes
"""
from os.path import split

FILENAME = "wimbledon.csv"


def main():
    print("Wimbledon Champions:")
    year_details = get_year_details()
    countries, name_to_wins = get_winning_details(year_details)
    print_winner_victories(name_to_wins)
    print_countries(countries)


def print_countries(countries):
    print(f"\nThese {len(countries)} have won Wimbledon:\n{", ".join(sorted(countries))}")


def print_winner_victories(name_to_wins):
    for name, number_of_wins in name_to_wins.items():
        print(f"{name} {number_of_wins}")


def get_winning_details(year_details: list) -> tuple:
    name_to_wins = {}
    countries = set()
    for year in year_details:
        name = year[2]
        country = year[3]
        countries.add(country)
        if name in name_to_wins:
            name_to_wins[name] += 1
        else:
            name_to_wins[name] = 1
    return countries, name_to_wins


def get_year_details() -> list:
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        year_details = []
        for line in in_file:
            year_details.append(line.split(","))
    return year_details


main()
