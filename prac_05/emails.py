"""
Emails
Estimate: 30 minutes
Actual:   ?? minutes
"""


def main():
    """Get email and name and stor as a dictionary"""
    email = input("Email: ")
    email_to_name = {}
    while email != "":
        name = extract_name(email)
        correct_name = input(f"Is your name {name}? (Y/n) ").upper()
        if correct_name not in ("Y", ""):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email: str):
    """Extract the name for the email"""
    separate_email = email.split("@")
    name = " ".join(separate_email[0].split(".")).title()
    return name


main()
