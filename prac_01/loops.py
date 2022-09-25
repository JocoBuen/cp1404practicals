# display the odd number from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for i in range(20, 0 , -1):
    print(i, end=' ')
print()

# c. print n stars
stars = int(input("Number of stars: "))
for star in range(0, stars, 1):
    print("*", end='')

# d. print n lines of increasing stars
stars = int(input("\nNumber of stars: "))
for star in range(0, stars, 1):
    for n in range(0, star + 1, 1):
        print("*",end='\n')
