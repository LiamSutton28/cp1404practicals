
def main():
    length_of_password = 8
    password = get_password(length_of_password)
    print_password(password)


def print_password(password: str):
    print("*" * len(password))


def get_password(length_of_password: int) -> str:
    password = input("Provide a password: ")
    while len(password) <= length_of_password:
        print("Password must be longer")
    return password


main()