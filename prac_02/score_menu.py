""""""
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

print(MENU)
choice = input("->").upper()
while choice != "Q":
    if choice == "P":
        <do first task>
    elif choice == "S"
        <do second task>
    else
        print("Invalid input")
    print(MENU)
    choice = input("->").upper()

print("Farewell")