"""
QUESTION:
Implement a MeasurementConverter class with methods `__init__(self, quantity, unit)`, `convert_to(self, new_unit)`, and `change_quantity(self, new_quantity)`. The class should be able to convert between 'poles', 'lines', 'rakes', and 'radians' units of measurement using the following conversion rates: 1 pole = 5 lines, 1 line = 15 rakes, 1 rake = 0.0174533 radians. The class should handle unsupported units and return an error message in such cases. The `__init__` method initializes the class with a quantity and its unit, `convert_to` method converts the quantity to the specified unit, and `change_quantity` method updates the quantity.
"""

def MeasurementConverter(quantity, unit):
    conversion_rates = {
        'poles': {'lines': 5, 'rakes': 5 * 15, 'radians': 5 * 15 * 0.0174533},
        'lines': {'poles': 1/5, 'rakes': 15, 'radians': 15 * 0.0174533},
        'rakes': {'poles': 1/(5*15), 'lines': 1/15, 'radians': 0.0174533},
        'radians': {'poles': 1/(5*15*0.0174533), 'lines': 1/(15*0.0174533), 'rakes': 1/0.0174533}
    }

    class Measurement:
        def __init__(self, quantity, unit):
            self.quantity = quantity
            self.unit = unit

        def convert_to(self, new_unit):
            if new_unit not in conversion_rates[self.unit]:
                return "Unsupported unit"
            converted_quantity = self.quantity * conversion_rates[self.unit][new_unit]
            return converted_quantity

        def change_quantity(self, new_quantity):
            self.quantity = new_quantity

    return Measurement(quantity, unit)