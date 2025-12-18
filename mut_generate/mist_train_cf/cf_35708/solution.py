"""
QUESTION:
Implement a function named `process_state` that takes a dictionary of states with their attributes as input and returns a new dictionary with the following modifications: 

- The population is converted to millions (divided by 1,000,000) and rounded to two decimal places.
- The names of the capital cities and the largest cities are capitalized.
- A new key-value pair is added for each state with the key 'density' and the value as the population density (population divided by 150,000 square miles). 

Assume that the input dictionary is not empty and the land area for each state is 150,000 square miles.
"""

def process_state(state: dict) -> dict:
    modified_state = {}
    for state_name, state_info in state.items():
        modified_info = {
            'population': round(state_info['population'] / 1000000, 2),
            'capital': state_info['capital'].capitalize(),
            'largest_city': state_info['largest_city'].capitalize(),
            'abbreviation': state_info['abbreviation'],
            'density': round(state_info['population'] / 150000, 2)
        }
        modified_state[state_name] = modified_info
    return modified_state