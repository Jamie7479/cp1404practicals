"""Taxi Simulator Exercise"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").strip().lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            try:
                current_taxi = taxis[int(input("Choose taxi: "))]
            except (IndexError, ValueError):
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                current_taxi.drive(int(input("Drive how far? ")))
                fare = current_taxi.get_fare()
                total_bill += fare
                print(f"Your {current_taxi.name} trip will cost you ${fare:,.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:,.2f}")
        print(MENU)
        choice = input(">>> ").strip().lower()
    print(f"Totat trip cost: ${total_bill:,.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()