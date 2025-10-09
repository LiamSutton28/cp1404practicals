"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
from itertools import accumulate


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)
    totals = calculate_cumulative_income(incomes, number_of_months)
    print_report(incomes, number_of_months, totals)


def print_report(incomes: list[float], number_of_months: int, totals: list[float]):
    """ Print income report function"""
    print("\nIncome Report\n-------------")
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total = totals[month - 1]
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def calculate_cumulative_income(incomes: list[float], number_of_months: int):
    accumulative_total = 0
    totals = []
    for month in range(1, number_of_months + 1):
        accumulative_total += incomes[month - 1]
        totals.append(accumulative_total)
    return totals


main()
