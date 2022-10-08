import random

NUMBERS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
           30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)


def main():
    number_of_pick = int(input("How many quick picks to generate: "))
    for pick in range(number_of_pick):
        picks = []
        for i in range(6):
            random_pick = check_if_random_pick_is_repeated(picks)
            picks.append(random_pick)
        picks.sort()
        display_picks(picks)
        picks.clear()


def check_if_random_pick_is_repeated(picks):
    random_pick = (random.choice(NUMBERS))
    while random_pick in picks:
        random_pick = (random.choice(NUMBERS))
    return random_pick


def display_picks(random_picks):
    for i in range(6):
        print(f"{random_picks[i]:>2}", end=" ")
    print()


main()
