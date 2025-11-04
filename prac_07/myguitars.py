"""
Prac 7
Read Guitars from File, add new and Display
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from file, add new guitars, display and write to file"""
    guitars = []
    create_guitar_objects(guitars, FILENAME)
    add_new_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    write_guitars_to_file(guitars, FILENAME)


def create_guitar_objects(guitars, filename):
    """Read guitars from file, add guitar objects to guitars list"""
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))


def add_new_guitars(guitars):
    """Add new guitars using user input"""
    print("Add new guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")


def write_guitars_to_file(guitars, filename):
    """Write guitars to file"""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    """Display all guitars"""
    max_name_length = max((len(guitar.name) for guitar in guitars))
    for guitar in guitars:
        print(f"{guitar.name:{max_name_length}} ({guitar.year:4}): ${guitar.cost:,.2f}")


main()
