"""
QUESTION:
Create a function called `create_dict` that takes a list of integers as input and returns a dictionary where each key is an element from the list and its corresponding value is the sum of its indices from all occurrences in the list. If an element appears only once in the list, its value in the dictionary should be its index.
"""

def create_dict(lst):
    result_dict = {}
    for i, key in enumerate(lst):
        if key in result_dict:
            result_dict[key] += [i]
        else:
            result_dict[key] = [i]
    
    # Create a new dictionary with the values as the sum of the corresponding values from all occurrences
    final_dict = {}
    for key, value_list in result_dict.items():
        final_dict[key] = sum(value_list)
    
    return final_dict