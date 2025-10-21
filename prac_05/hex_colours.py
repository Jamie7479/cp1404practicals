"""
CP1404/CP5632 Practical
Hex values in a dictionary, with english keys
"""

NAME_TO_HEX = {"Alizarin Crimson": "#e32636", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Asparagus": "#87a96b", "Baby Pink": "#f4c2c2",
               "Boysenberry": "#873260", "Bronze": "#cd7f32", "Burgundy": "#800020", "Burnt Sienna": "#e97451", "Cadmium Green": "#006b3c"}

print(NAME_TO_HEX)

name = input("Enter colour name: ").title().strip()
while name != "":
    try:
        print(f"{name} is {NAME_TO_HEX[name]}")
    except KeyError:
        print("Invalid colour name")
    name = input("Enter colour name: ").title().strip()
