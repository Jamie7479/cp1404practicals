"""Get a password with minimum length and print asterisks"""

MIN_PASSWORD_LENGTH = 5


def main():
    """Get a password with minimum length and print asterisks"""
    password = get_password()

    print_password(password)


def get_password():
    """Get password with minimum length"""
    password = input("Password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be greater than {MIN_PASSWORD_LENGTH} characters")
        password = input("password: ")
    return password


def print_password(password):
    """Print as many asterisks as characters in inputted password"""
    print("*" * len(password))


main()
