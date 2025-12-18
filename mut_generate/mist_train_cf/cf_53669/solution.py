"""
QUESTION:
Create a function `merge_fruits` that takes two lists of strings `arr1` and `arr2`, and a dictionary `spell_dict` as input. The function should merge the two lists, removing duplicates, and return a list of tuples, where each tuple contains a fruit from the merged list and the spelled-out number of its letters. The resulting list should be in alphabetical order. The `spell_dict` dictionary will be used to spell out the number of letters. The dictionary will contain integer keys from 1 to 10 and their corresponding spelled-out string values.
"""

def merge_fruits(arr1, arr2, spell_dict):
    # Merge the arrays and remove duplicates
    merged = sorted(list(set(arr1 + arr2)))
    
    # Create the resulting array of tuples
    return [(fruit, spell_dict[len(fruit)]) for fruit in merged if len(fruit) <= 10]