""" Quick picks program"""

import random

AMOUNT_OF_NUMBERS = 6
MINIMUM_LIMIT = 1
MAXIMUM_LIMIT = 45

number_of_picks = int(input("How many quick picks? "))
total_numbers = []
for i in range(number_of_picks):
    quick_pick_numbers = []
    for j in range(AMOUNT_OF_NUMBERS):
        random_number = random.randint(MINIMUM_LIMIT, MAXIMUM_LIMIT)
        while random_number in quick_pick_numbers:
            random_number = random.randint(MINIMUM_LIMIT, MAXIMUM_LIMIT)
        quick_pick_numbers.append(random_number)
    quick_pick_numbers.sort()
    for j in range(AMOUNT_OF_NUMBERS):
        print("{:3}".format(quick_pick_numbers[j]), end="")
    print("")
