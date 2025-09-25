""" Score Menu """

MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    score = float(input("Submit a score: "))
    while not is_valid(score):
        print("Invalid score. Need a number between 0 and 100")
        score = float(input("Submit a score: "))
    print(MENU)
    choice = input(">> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Submit a score: "))
            while not is_valid(score):
                print("Invalid score. Need a number between 0 and 100")
                score = float(input("Submit a score: "))
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print_stars(score)
        print(MENU)
        choice = input(">> ").upper()
    print("Farewell")


def print_stars(score: float):
    print("*" * round(score))


def is_valid(score):
    return 0 <= score <= 100


def determine_score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
