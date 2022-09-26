"""
get password
while length of password < 6 or blank in password
    display Invalid password
star_password = length of password * "*"
display star_password
"""
users_password = input("Enter password: ")
while len(users_password) < 6 or " " in users_password:
    print("Invalid Password")
    users_password = input("Enter password: ")
print("*" * len(users_password))
