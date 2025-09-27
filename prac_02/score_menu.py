""""""
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input("->").upper()
    while choice != "Q":
        if choice == "G":
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
    score = int(input("Score: "))
    while score < 0 or score > 100:
        score = int(input("Score: "))
    return score

def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()