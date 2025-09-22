from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight: int = 1000
    started: bool = False
    fuel: int = 50
    fuel_consumption: int = 10

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Fuel is low")

    def move(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel("Not enough fuel")