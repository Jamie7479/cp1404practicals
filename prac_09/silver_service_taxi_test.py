from silver_service_taxi import SilverServiceTaxi

tests = [SilverServiceTaxi("Hummer", 200, 2),
         SilverServiceTaxi("test2", 200, 4),
         SilverServiceTaxi("test3", 200, 1)]

# fares = [48.78, 93.06, 26.64] # calculated fares
fares = [48.8, 93.1, 26.6]

for i, test in enumerate(tests):
    print(test)
    test.drive(18)
    fare = test.get_fare()
    print(fare)
    assert fare == fares[i]
