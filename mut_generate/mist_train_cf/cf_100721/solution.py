"""
QUESTION:
Create a function called `calculate_carbon_emissions` that takes three parameters: `population`, `income_per_capita`, and `carbon_intensity`. The function should calculate the total carbon emissions using the formula `E = P * I * C` and return the result. 

Restrictions: The function should not take any other parameters besides the three specified. The function should not perform any input validation or error checking.
"""

def calculate_carbon_emissions(population, income_per_capita, carbon_intensity):
    return population * income_per_capita * carbon_intensity