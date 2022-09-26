"""
get password
while length of password < 6 or blank in password
    display Invalid password
star_password = length of password * "*"
display star_password
"""


def main():
    password = get_password()
    display_password_in_asterisk(password)


def display_password_in_asterisk(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < 6 or " " in password:
        print("Invalid Password")
        password = input("Enter password: ")
    return password


main()
