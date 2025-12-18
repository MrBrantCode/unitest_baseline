"""
QUESTION:
Create a function `battery_efficiency` for the `ElectricVehicle` class. The function should calculate the battery efficiency of the electric vehicle based on its battery capacity, battery charge, and total driven distance, where efficiency is defined as miles driven per kWh of energy consumed. The `ElectricVehicle` class should have the following properties: `battery_capacity`, `battery_charge`, and `total_driven_distance`. The function should return the battery efficiency.
"""

def battery_efficiency(battery_capacity, battery_charge, total_driven_distance):
    # Miles per KWH
    return total_driven_distance / (battery_capacity - battery_charge)