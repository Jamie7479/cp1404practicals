from car import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=100.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0,100) < self.reliability:
            super().drive(distance)
        else:
            return 0
