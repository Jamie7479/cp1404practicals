MIN_PASSWORD_LENGTH = 5


def main():
    password = get_password()

    print_password(password)


def get_password():
    password = input("Password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be greater than {MIN_PASSWORD_LENGTH} characters")
        password = input("password: ")
    return password


def print_password(password):
    print("*" * len(password))


main()
