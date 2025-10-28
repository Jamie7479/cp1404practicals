"""
Get and display guitars
Estimated time: 20mins
Start time: 1.25
Duration: 20mins
"""

from guitar import Guitar


def main():
    """Get and display guitars"""
    guitars = []
    print("My guitars!")

    get_guitars(guitars)
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    display_guitars(guitars)


def get_guitars(guitars):
    """Get guitars"""
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added")
        name = input("Name: ")


def display_guitars(guitars):
    """Display guitars"""
    print("These are my guitars:")
    max_name_length = max((len(guitar.name) for guitar in guitars))
    max_cost_length = max((len(f"{guitar.cost:,.2f}") for guitar in guitars))
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""

        print(
            f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:{max_cost_length},.2f} {vintage_string}")


main()
