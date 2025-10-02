""" file program """

FILENAME = "name.txt"

# 1
provided_name = input("Name: ")
out_file = open(FILENAME, 'w')
print(provided_name, file=out_file)
out_file.close()

# 2
infile = open(FILENAME)
found_name = infile.readline().strip()
print(f"Hi {found_name}")
infile.close()
