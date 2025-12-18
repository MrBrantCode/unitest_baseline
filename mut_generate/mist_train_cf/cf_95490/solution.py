"""
QUESTION:
Write a function `count_elements` that takes a dictionary as input and returns the number of elements in the dictionary, excluding any elements whose keys are numbers or whose values are not dictionaries. If a value is a dictionary, count the number of elements in that dictionary as well. The function should handle cases where the dictionary is empty or where the dictionary values are themselves dictionaries or lists.
"""

def count_elements(dictionary):
    count = 0
    
    # Iterate through the key-value pairs in the dictionary
    for key, value in dictionary.items():
        # Exclude elements whose keys are numbers or whose values are dictionaries
        if not isinstance(key, int) and not isinstance(value, dict):
            # If the value is a nested dictionary, count the elements in that dictionary as well
            if isinstance(value, dict):
                count += count_elements(value)
            else:
                count += 1
        # Count elements in nested dictionaries
        elif isinstance(value, dict):
            count += count_elements(value)
    
    return count