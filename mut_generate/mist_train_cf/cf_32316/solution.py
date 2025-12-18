"""
QUESTION:
Write a function `update_production_data(raw_data, GENERATION_MAPPING, initial_production)` that updates the production data by aggregating the energy values from `raw_data` based on the `GENERATION_MAPPING`. The `raw_data` is a dictionary where keys are energy sources and values are dictionaries with an energy value. The `GENERATION_MAPPING` is a dictionary that maps energy sources to production categories. The `initial_production` is a dictionary with initial energy values for each production category. The function should return the updated production data, ignoring negative energy values.
"""

def update_production_data(raw_data, GENERATION_MAPPING, initial_production):
    production_data = initial_production.copy()
    for from_key, to_key in GENERATION_MAPPING.items():
        production_data[to_key] = production_data.get(to_key, 0) + max(0, raw_data.get(from_key, {}).get("value", 0))
    return production_data