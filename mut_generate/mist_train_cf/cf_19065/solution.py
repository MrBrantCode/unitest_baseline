"""
QUESTION:
Write a function `count_elements(dictionary)` that returns the number of elements in a dictionary, excluding any elements whose keys are numbers or whose values are not dictionaries. If a value is a dictionary, count the number of elements in that dictionary as well. The function should handle empty dictionaries and dictionaries with nested dictionary values.
"""

def count_elements(dictionary):
    count = 0
    
    # Iterate through the key-value pairs in the dictionary
    for key, value in dictionary.items():
        # Exclude elements whose keys are numbers or whose values are dictionaries
        if not isinstance(key, int) and isinstance(value, dict):
            # If the value is a nested dictionary, count the elements in that dictionary as well
            count += count_elements(value)
        elif not isinstance(key, int) and not isinstance(value, dict):
            count += 1
    
    return count