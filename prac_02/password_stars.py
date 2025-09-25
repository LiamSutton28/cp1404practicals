
length_of_password = 8
password = input("Provide a password: ")
while len(password) <= length_of_password:
    print("Password must be longer")
print("*" * len(password))