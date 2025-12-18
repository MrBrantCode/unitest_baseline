"""
QUESTION:
Write a function called `generate_combinations` that generates and returns all possible unique combinations of three lists: `climate_models`, `regional_models`, and `emission_scenarios`. 

The `climate_models` list contains the strings 'EC-EARTH', 'GFDL-ESM2M', 'HadGEM2-ES', 'MIROC-ESM-CHEM', 'NorESM1-M'. The `regional_models` list contains the strings 'RACMO22E', 'WRF', 'RegCM4', 'COSMO-CLM'. The `emission_scenarios` list contains the strings 'rcp2.6', 'rcp4.5', 'rcp6.0', 'rcp8.5'. 

The function should return a list of tuples, where each tuple represents a unique combination of a climate model, a regional climate model, and a greenhouse gas emission scenario.
"""

import itertools

def generate_combinations(climate_models, regional_models, emission_scenarios):
    """
    Generates and returns all possible unique combinations of three lists: 
    climate_models, regional_models, and emission_scenarios.

    Args:
    climate_models (list): A list of climate models.
    regional_models (list): A list of regional climate models.
    emission_scenarios (list): A list of greenhouse gas emission scenarios.

    Returns:
    list: A list of tuples, where each tuple represents a unique combination of 
    a climate model, a regional climate model, and a greenhouse gas emission scenario.
    """
    return list(itertools.product(climate_models, regional_models, emission_scenarios))