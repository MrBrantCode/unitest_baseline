"""
QUESTION:
Write a function called `calculate_total_emissions` that calculates the total carbon emissions for each energy source, taking into account the emissions from manufacturing, transportation, and maintenance, as well as any carbon savings from using the energy source.

The function should accept a dictionary of energy sources where each key is the name of the energy source and each value is another dictionary with the following keys: 'emissions', 'savings', 'manufacturing', 'transportation', and 'maintenance'. The values for these keys should be the corresponding carbon emissions or savings for each energy source, measured in metric tons CO2e.

The function should return a dictionary where the keys are the names of the energy sources and the values are the total carbon emissions for each energy source.
"""

def calculate_total_emissions(energy_sources):
    """
    Calculate the total carbon emissions for each energy source.

    Args:
    energy_sources (dict): A dictionary of energy sources where each key is the name of the energy source
                           and each value is another dictionary with the following keys: 'emissions', 'savings', 
                           'manufacturing', 'transportation', and 'maintenance'.

    Returns:
    dict: A dictionary where the keys are the names of the energy sources and the values are the total carbon emissions for each energy source.
    """
    total_emissions = {}
    for source, emissions_data in energy_sources.items():
        total_emission = (emissions_data['emissions'] + emissions_data['manufacturing'] + 
                          emissions_data['transportation'] + emissions_data['maintenance'] - 
                          emissions_data['savings'])
        total_emissions[source] = total_emission
    return total_emissions