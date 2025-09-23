MIN_PASSWORD_LENGTH = 5

password = input("Password: ")
length = len(password)
while length < MIN_PASSWORD_LENGTH:
    print(f"Password must be greater than {MIN_PASSWORD_LENGTH} characters")
    password = input("password: ")
    length = len(password)

print("*" * length)
