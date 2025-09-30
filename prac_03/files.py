"""
Writing and reading files exercises
"""

# 1.
name = input("What is your name? ")
out_file = open("name.txt", 'w')
out_file.write(name)
out_file.close()

# 2.
in_file = open("name.txt")
print(f"Hi {in_file.read()}!")
in_file.close()

# 3.
with open("numbers.txt") as in_file:
    print(int(in_file.readline()) + int(in_file.readline()))

# 4.
total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        total += int(line)
print(total)
