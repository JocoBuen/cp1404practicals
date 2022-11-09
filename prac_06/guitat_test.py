from prac_06.guitar import Guitar

CURRENT_YEAR = 2022


def run_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {5}. Got {guitar.get_age()}")
    print()
    print(f"{guitar.name} is vintage - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is vintage - Expected {False}. Got {guitar.is_vintage()}")


if __name__ == "__main__":
    run_test()
