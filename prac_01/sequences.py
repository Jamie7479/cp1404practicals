x = int(input("Value 1: "))
y = int(input("Value 2: "))

print("""1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program""")

choice = input()
while choice != "4":
    if choice == "1":
        for i in range(x, y):
            if i % 2 == 0:
                print(i, end=" ")
        print()

    elif choice == "2":
        for i in range(x, y):
            if i % 2 == 1:
                print(i, end=" ")
        print()
    elif choice == "3":
        for i in range(x, y, 1):
            print(i ** 2, end=" ")
        print()
    else:
        print("Invalid input")
    print("""1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)
4. Exit the program""")
    choice = input()

print("Finished")
