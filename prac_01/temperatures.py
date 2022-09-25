"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

display MENU
get users_choice
whiele users_choice != Q
    if users_choice is C
        get celcius
        fahrenheit = celcius * 0.9 / 5 + 32
        display Result: fahrenheit
    else if users_choice is F
        get fahrenheit
        celcius = 5 / 9 * (fahrenheit - 32)
        display Result celcius
    else
        display Invalid option
    display MENU
    get users_choice
display Thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
users_choice = input(">>> ").upper()
while users_choice != "Q":
    if users_choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif users_choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit = float(input("Farenheit: "))
        celsius = 5 /9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    users_choice = input(">>> ").upper()
print("Thank you.")