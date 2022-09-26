"""
Score menu program
S - get valid_score
P - display score remarks
G - display asterisk
Q - Quit

display MENU
get choice
while choice != "Q"
    if choice == "S":
        score = get_valid_score
    elif choice == "P"
        determine_score(score)
    elif choice == "G"
        print_asterisk(score)
    else:
        print("Invalid input")
    choice = input(">>>").upper()
display Thank you


function get_valid_score
    get score
    while score > 100 or 0 > score
        display invalid score
        get score
    return score


function determine_score(score)
    if score > 100 or score < 0
        return "Invalid score"
    else if score >= 90
        return "Excellent"
    else if score >= 50
        return "Passable"
    else
        return "Bad"

function print_asterisk(score)
    display("*" * score)
"""

MENU = """S - Get the score
P - Display score remarks
G - Display score with asterisk
Q - Quit"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "S":
            score = get_valid_score()
        elif choice == "P":
            print(f"The score {score} is {determine_score(score)}")
        elif choice == "G":
            print_asterisk(score)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


# This function will determine the score
def determine_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# This function will determine if score is valid
def get_valid_score():
    score = int(input("Enter score: "))
    while score > 100 or 0 > score:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


# This function will display asterisk
def print_asterisk(score):
    print("*" * score)


main()
