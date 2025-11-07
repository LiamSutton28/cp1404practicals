"""
Guitars
Estimate: 40 minutes
Actual:   30 minutes
"""
from prac_06.guitar import Guitar

print("My guitars!")
# guitars = []
# name = input("Name: ")
# while name != "":
#     year = int(input("Year: "))
#     cost = float(input("Cost: ")[1:])
#     guitars.append(Guitar(name,year,cost))
#     print(f"{name} ({year:4}) : $ {cost:,.2f} added.")
#     name = input("Name: ")
guitars = [Guitar("Fender Stratocaster", 2014, 765.4), Guitar("Gibson L-5 CES", 1922, 16035.40),
           Guitar("Line 6 JTV-59", 2010, 1512.9)]
for i, guitar in enumerate(guitars):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20}({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


