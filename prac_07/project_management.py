from prac_07.project import Project

FILENAME = 'projects.txt'
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects
- (A)dd new project
- (U)pdate project
- (Q)uit"""

projects = []

print(MENU)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "l":
        in_file = open(FILENAME, 'r')
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project_to_add = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project_to_add)
        in_file.close()

    elif choice == "s":
        pass
    elif choice == "d":
        incomplete_projects = []
        complete_projects = []
        if projects:
            projects.sort()
            for project in projects:
                if project.is_complete():
                    complete_projects.append(project)
                else:
                    incomplete_projects.append(project)
            print("Incomplete Projects")
            for i in incomplete_projects:
                print(i)
            print("Complete Projects")
            for i in complete_projects:
                print(i)

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
