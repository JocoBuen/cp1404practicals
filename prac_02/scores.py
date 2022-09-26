"""
score status program
import random

get score
display score
generate random_score
display random_score

function determine_score
    if score > 100 or score < 0
        return "Invalid score"
    else if score >= 90
        return "Excellent"
    else if score >= 50
        return "Passable"
    else
        return "Bad"

"""
import random


def main():
    score = float(input("Enter score: "))
    print(f"The score {score} is {determine_score(score)}")
    random_score = random.randint(1, 100)
    print(f"The random score {random_score} is {determine_score(random_score)}")


def determine_score(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
