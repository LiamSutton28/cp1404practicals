""" file program """

FILENAME = "name.txt"

# 1
name = input("Name: ")
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()
