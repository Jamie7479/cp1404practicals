"""
Guitar Class
Estimated time: 2mins
Start time: 1.00
End time:
Duration: 10mins
"""
from guitar import Guitar

guitar_test1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_test2 = Guitar("Other guitar", 2023, 100)

print(f"{guitar_test1.name} get_age() - Expected 103. Got {guitar_test1.get_age()}")
print(f"{guitar_test2.name} get_age() - Expected 2. Got {guitar_test2.get_age()}")
print(f"{guitar_test1.name} is_vintage() - Expected True. Got {guitar_test1.is_vintage()}")
print(f"{guitar_test2.name} is_vintage() - Expected False. Got {guitar_test2.is_vintage()}")

