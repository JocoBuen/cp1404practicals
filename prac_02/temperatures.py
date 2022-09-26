"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

display MENU
get users_choice
while users_choice != Q
    if users_choice is C
        get celsius
        fahrenheit = celsius * 0.9 / 5 + 32
        display Result: fahrenheit
    else if users_choice is F
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        display Result celsius
    else
        display Invalid option
    display MENU
    get users_choice
display Thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    users_choice = input(">>> ").upper()
    while users_choice != "Q":
        if users_choice == "C":
            convert_celsius_to_fahrenheit()
        elif users_choice == "F":
            convert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        users_choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


main()
