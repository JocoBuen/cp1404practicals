name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
for line in in_file:
    print(f"Your name is {line}")
in_file.close()

in_file = open("numbers.txt", "r")
numbers = []
for line in in_file:
    numbers = in_file.readlines()
in_file.close()
print(int(numbers[0]) + int(numbers[1]))

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(total)
