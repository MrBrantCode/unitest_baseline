"""
QUESTION:
Implement a Python function `calculate_total_impact` that calculates the total impact of emissions considering the climate feedback effect. The function takes four parameters: 
- `emissions_data`: a dictionary containing the emissions data for CH4, CO, NMVOC, and NOx.
- `beta`: a list of coefficients for CH4, CO, NMVOC, and NOx.
- `PI`: a list of reference parameters for CH4, CO, NMVOC, and NOx.
- `temperature`: the temperature for which the climate feedback effect needs to be considered.

Assume the emissions data, beta, and PI are of the same length and contain valid numerical values. Use the given `temperature_feedback` function in the calculation.
"""

def calculate_total_impact(emissions_data, beta, PI, temperature):
    """
    Calculate the total impact of emissions considering the climate feedback effect.

    Parameters:
    emissions_data (dict): A dictionary containing the emissions data for CH4, CO, NMVOC, and NOx.
    beta (list): A list of coefficients for CH4, CO, NMVOC, and NOx.
    PI (list): A list of reference parameters for CH4, CO, NMVOC, and NOx.
    temperature (float): The temperature for which the climate feedback effect needs to be considered.

    Returns:
    float: The total impact of emissions considering the climate feedback effect.
    """
    def temperature_feedback(T, a=0.03189267, b=1.34966941, c=-0.03214807):
        if T <= 0:
            return 0
        else:
            return a * T**2 + b * T + c

    total_impact = 0
    for i, (emission, coefficient, reference) in enumerate(zip(emissions_data.values(), beta, PI)):
        impact = coefficient * (emission - reference)
        total_impact += impact * temperature_feedback(temperature)
    return total_impact