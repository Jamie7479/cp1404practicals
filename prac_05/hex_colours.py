"""
CP1404/CP5632 Practical
Hex values in a dictionary, with english keys
"""

NAME_TO_HEX = {"alizarincrimson": "#e32636", "amber": "#ffbf00", "amethyst": "#9966cc", "asparagus": "#87a96b", "babypink": "#f4c2c2",
               "boysenberry": "#873260", "bronze": "#cd7f32", "burgundy": "#800020", "burntsienna": "#e97451", "cadmiumgreen": "#006b3c"}

print(NAME_TO_HEX)

name = input("Enter colour name: ").lower()
while name != "":
    try:
        print(name, "is", NAME_TO_HEX[name])
    except KeyError:
        print("Invalid colour name")
    name = input("Enter colour name: ").lower()
