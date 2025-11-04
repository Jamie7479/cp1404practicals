"""
Prac 7
Read Guitars from File and Display
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = []
    create_guitar_objects(guitars, FILENAME)
    guitars.sort()


def create_guitar_objects(guitars, filename):
    with open(filename, "r", newline="") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))


main()
