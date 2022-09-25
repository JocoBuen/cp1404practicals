"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("Enter name: ")
users_choice = input("MENU:\n(H)ello \n(G)oodbye \n(Q)uit \n>>> ").upper()

while users_choice != "Q":
    if users_choice == "H":
        print("Hello {}".format(name))
    elif users_choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid choice")
    users_choice = input("MENU:\n(H)ello \n(G)oodbye \n(Q)uit \n>>> ").upper()

print("Finished.")
