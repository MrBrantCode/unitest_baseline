"""
QUESTION:
Create a function `calculate_fuel` that calculates the amount of fuel required based on the weight and fuel efficiency. The weight and fuel efficiency of each part are given: engine (500 kg, 0.2 km/kg), chassis (1000 kg, 0.1 km/kg), and body (1500 kg, 0.05 km/kg). Use the formula fuel = weight / fuel_efficiency to calculate the fuel required for each part. The function should return the fuel required for the given part.
"""

def calculate_fuel(weight, fuel_efficiency):
    """
    Calculate the fuel required based on the weight and fuel efficiency.

    Args:
        weight (float): The weight of the part in kg.
        fuel_efficiency (float): The fuel efficiency of the part in km/kg.

    Returns:
        float: The fuel required for the given part in kg/km.
    """
    return weight / fuel_efficiency