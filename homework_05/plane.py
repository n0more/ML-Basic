"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo <= self.max_cargo:
            self.cargo += new_cargo
        else:
            raise CargoOverload("Cargo overload")

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before