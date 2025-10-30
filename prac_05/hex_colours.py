"""Hex Colours program"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                  "Amethyst": "#9966cc", "Antique White": "#faebd7", "Antique White1": "#ffefdb", "Antique White2": "#eedfcc"}

for colour, code in COLOUR_TO_CODE.items():
    print(f"{colour:{max(len(code) for code in COLOUR_TO_CODE)}} is {code}")

hex_colour = input("Enter colour: ").title()
while hex_colour != "":
    try:
        print(hex_colour, "is", COLOUR_TO_CODE[hex_colour])
    except KeyError:
        print("Invalid colour")
    hex_colour = input("Enter colour: ").title()
print("Goodbye")
