number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total = 0
for i in range(number_of_items):
    total += float(input("Price of item: "))
if total > 100:
    total *= 0.9
print(f"Total price for {number_of_items} items is ${total:.2f}")
