"""
QUESTION:
Create a function named `retrieve_values` that takes two parameters: a list of dictionaries `dict_list` and a character `starting_letter`. The function should return a list of values where each value corresponds to the first value in a dictionary that has a key starting with `starting_letter`. If no key in a dictionary meets the condition, the function should return "No Match" for that dictionary.
"""

def retrieve_values(dict_list, starting_letter):
    output = []
    for dict in dict_list:
        filtered_items = [value for key, value in dict.items() if key.startswith(starting_letter)]
        output.append(filtered_items[0] if filtered_items else 'No Match')
    return output