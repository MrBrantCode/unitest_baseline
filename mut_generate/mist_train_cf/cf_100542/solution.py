"""
QUESTION:
Create a function `calculate_energy_emissions` that takes a dictionary of energy sources as input, where each energy source is a dictionary containing the keys 'emissions', 'savings', 'manufacturing', 'transportation', and 'maintenance'. The function should return a dictionary with the total emissions for each energy source, calculated as the sum of emissions, manufacturing, transportation, and maintenance, minus the savings.
"""

def calculate_energy_emissions(energy_sources):
    """
    Calculate the total emissions for each energy source.

    Args:
        energy_sources (dict): A dictionary of energy sources where each energy source is a dictionary containing the keys 'emissions', 'savings', 'manufacturing', 'transportation', and 'maintenance'.

    Returns:
        dict: A dictionary with the total emissions for each energy source.
    """
    total_emissions = {}
    for source, data in energy_sources.items():
        total_emissions[source] = data['emissions'] + data['manufacturing'] + data['transportation'] + data['maintenance'] - data['savings']
    return total_emissions