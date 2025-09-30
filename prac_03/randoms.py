"""
Generate various random numbers
"""

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# 1. Smallest is 5, largest 20
# 2. Smallest 3, largest 9. It could not produce a 4 as the step is 2 meaning only the odd numbers can be produced
# 3. Smallest 2.5, largest 5.5

# assuming it wants an integer
print(random.randint(1, 100))
