"""
Emails
Estimate: 10 minutes
Actual:   12 minutes
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    name = " ".join(email.split("@")[0].split(".")).title()
    choice = input(f"Is your name {name}? (Y/n) ").lower()
    if choice == "y" or choice == "":
        email_to_name[email] = name
    else:
        email_to_name[email] = input("Name: ")
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
