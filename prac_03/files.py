""" file program """

FILENAME = "name.txt"

# 1
provided_name = "Liam"  # input("Name: ")
out_file = open(FILENAME, 'w')
print(provided_name, file=out_file)
out_file.close()

# 2
infile = open(FILENAME)
found_name = infile.read().strip() #reads entire file and strips white space
print(f"Hi {found_name}")
infile.close()

# 3
with open("numbers.txt") as in_file:
    number1 = int(in_file.readline()) # reads one line of code and stores it
    number2 = int(in_file.readline())
print(number1 + number2)

#4
sum_of_all_lines = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        number = int(line)      # reads every line in the file and saves it as number
        sum_of_all_lines += number  # adds number to the total which updates after every line
print(sum_of_all_lines)
