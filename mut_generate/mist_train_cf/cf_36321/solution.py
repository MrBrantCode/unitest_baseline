"""
QUESTION:
Create a `BeerContainer` class with the following attributes and methods, and a `calculate_inventory_value` function.

The `BeerContainer` class should have the following attributes:
- `container_type` (string)
- `quantity` (integer)
- `unit_price` (float)

The `BeerContainer` class should have the following methods:
- `__init__(self, container_type, quantity, unit_price)` to initialize the object
- `add_quantity(self, amount)` to add to the quantity
- `remove_quantity(self, amount)` to remove from the quantity, without going below 0
- `total_value(self)` to return the total value of the containers

The `calculate_inventory_value` function should take a list of `BeerContainer` objects and return the total value of the entire inventory.
"""

class BeerContainer:
    def __init__(self, container_type, quantity, unit_price):
        self.container_type = container_type
        self.quantity = quantity
        self.unit_price = unit_price

    def add_quantity(self, amount):
        self.quantity += amount

    def remove_quantity(self, amount):
        self.quantity = max(0, self.quantity - amount)

    def total_value(self):
        return self.quantity * self.unit_price

def calculate_inventory_value(beer_list):
    total_value = 0
    for beer in beer_list:
        total_value += beer.total_value()
    return total_value