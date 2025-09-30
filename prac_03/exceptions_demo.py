"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = getNonZeroDenominator()
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


def getNonZeroDenominator():
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    return denominator


main()

# 1. A ValueError will occur when a non-integer value is inputted, such as a float, or extra characters.
# 2. ZeroDivisionError will occur if the denominator input is 0
# 3. Check input first to ensure it isnt a 0
