"""
QUESTION:
Calculate the total energy distribution for a district based on the provided building data.

You are given dictionaries containing the number of buildings, percentage of agents, percentage of primary household heating (PHH) agents, and percentage of buildings engaged in agriculture for each building type, as well as the probability of district heating for each building type and the probability of photovoltaic (PV) plants in the district. Write a function `calculate_energy_distribution` to calculate the total energy distribution.

The function should take the following parameters:
- `buildings`: A dictionary containing the number of buildings for each type.
- `agents`: A dictionary containing the percentage of agents in each building type.
- `phh_agents`: A dictionary containing the percentage of PHH agents in each building type.
- `agriculture`: A dictionary containing the percentage of buildings engaged in agriculture for each building type.
- `dhn`: A dictionary containing the probability of district heating for each building type.
- `pv_plants`: The probability of PV plants in the district.

The function should return the total energy distribution for the district, which is the sum of energy distribution for each building type, calculated as the product of the number of buildings, the percentage of agents, the percentage of PHH agents, the probability of district heating, the probability of agriculture-based energy self-production, and the probability of PV plants.
"""

def calculate_energy_distribution(buildings, agents, phh_agents, agriculture, dhn, pv_plants):
    total_energy_distribution = 0
    for building_type in buildings:
        energy_distribution = buildings[building_type] * agents[building_type] * phh_agents[building_type] * agriculture[building_type] * dhn[building_type] * pv_plants
        total_energy_distribution += energy_distribution
    return total_energy_distribution