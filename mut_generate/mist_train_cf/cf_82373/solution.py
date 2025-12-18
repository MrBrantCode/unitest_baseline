"""
QUESTION:
Create a function named `nested_dict_counter` that takes a nested dictionary as input and returns the total count of all elements, including those in sub-dictionaries. The function should be able to handle cases where the input dictionary does not contain any nested dictionaries.
"""

def nested_dict_counter(nested_dict):
    count = 0
    for key in nested_dict:
        count += 1
        try:
            count += nested_dict_counter(nested_dict[key])
        except TypeError:
            pass
    return count