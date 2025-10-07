import random

MIN = 1
MAX = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    line = []
    for j in range(6):
        new_number = random.randint(MIN,MAX)
        while new_number in line:
            new_number = random.randint(MIN, MAX)
        line.append(new_number)
    print(" ".join(sorted((f"{number:2}" for number in line))))