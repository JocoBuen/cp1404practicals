"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When an invalid value to function was given by a user like string
2. When will a ZeroDivisionError occur? When the user give 0 as the divisor
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid divisor.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
