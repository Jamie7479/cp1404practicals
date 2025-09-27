"""Gets score (0-100) and can print score result, display as many asterisks as the score"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Gets score (0-100) and can print score result, display as many asterisks as the score"""
    score = get_valid_score()  # initial score value as other options require score to function
    print(MENU)
    choice = input("->").upper()
    while choice != "Q":
        if choice == "G":  # to change score
            score = get_valid_score()
        elif choice == "P":
            print(determine_grade(score))
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid input")
        print(MENU)
        choice = input("->").upper()

    print("Farewell")


def get_valid_score():
    """Get a valid score from 0-100"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        score = int(input("Score: "))
    return score


def determine_grade(score):
    """Return grade from score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
