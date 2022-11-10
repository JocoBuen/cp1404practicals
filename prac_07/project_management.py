from prac_07.project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects
- (A)dd new project
- (U)pdate project
- (Q)uit"""

# projects = []
# in_file = open(FILENAME, 'r')
# in_file.readline()
# for line in in_file:
#     parts = line.strip().split(',')
#     projects.append(parts)
# in_file.close()
#
# for project in projects:
#     print(project)

print(MENU)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "l":
        pass
    elif choice == "s":
        pass
    elif choice == "d":
        pass
    elif choice == "f":
        pass
    elif choice == "a":
        pass
    elif choice == "u":
        pass
    else:
        print("Invalid menu choice")
    print(MENU)
    choice = input(">>> ").lower()
