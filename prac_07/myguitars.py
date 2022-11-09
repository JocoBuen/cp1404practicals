from prac_06.guitar import Guitar
import csv

FILENAME = 'guitars.csv'


def main():
    guitars = []

    load_file(guitars)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    add_new_guitar(guitars)

    print(guitars)

    set_out_guitars(guitars)


def set_out_guitars(guitars):
    with open(FILENAME, 'w', encoding='UTF8', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(guitars)


def add_new_guitar(guitars):
    print("Enter new guitar.")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name:")


def load_file(guitars):
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


main()
