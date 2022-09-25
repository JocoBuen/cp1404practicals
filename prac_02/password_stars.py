"""Print grid program"""


def main():
    print_grid(3,7)


def print_grid(number_of_rows, number_of_columns):
    """Function docstring"""
    for row in range(0, number_of_rows, 1):
        for column in range(0, number_of_columns, 1):
            print("*", end="")
        print()


main()