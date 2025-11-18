from unreliable_car import UnreliableCar

ITERATIONS = 100000

tests = [UnreliableCar("Test1", ITERATIONS, 0),
         UnreliableCar("Test2", ITERATIONS, 30),
         UnreliableCar("Test3", ITERATIONS, 50),
         UnreliableCar("Test4", ITERATIONS, 70),
         UnreliableCar("Test5", ITERATIONS, 100)
         ]

for i in range(ITERATIONS):
    for test in tests:
        test.drive(1)
        # print(test1)

for test in tests:
    print(f"{test.name} Drive %: {100 * test.odometer / ITERATIONS}% - Reliability: {test.reliability}%")
