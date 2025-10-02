""" file program """

FILENAME = "name.txt"

# 1
provided_name = "Liam"  # input("Name: ")
out_file = open(FILENAME, 'w')
print(provided_name, file=out_file)
out_file.close()

# 2
infile = open(FILENAME)
found_name = infile.read().strip()
print(f"Hi {found_name}")
infile.close()

# 3
with open("numbers.txt") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)
