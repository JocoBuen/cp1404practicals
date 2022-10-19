"""
Emails
Estimate: 70 minutes
Actual:   83 minutes
"""


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = convert_email_to_name(email)
        action = input(f"Is your name {email_to_name.get(email)}? (Y/N) ").upper()
        if action == "N" or action == "NO":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def convert_email_to_name(email):
    parts = email.split("@")
    name = parts[0].split(".")
    name = " ".join(name).title()
    return name


main()
