"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint


def main():
    """Determine score status of inputted score and randomly generated score"""
    user_score = float(input("Enter score: "))
    print(determine_grade(user_score))
    random_score = randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_grade(random_score))


def determine_grade(score):
    """Determine grade from score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
