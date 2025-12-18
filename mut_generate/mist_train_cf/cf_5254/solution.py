"""
QUESTION:
Write a function named `compare_dictionaries` that takes two dictionaries as input and checks if they have the same keys and values. Each key should be a string, each value should be a positive integer, and each dictionary should not contain more than 10 key-value pairs. Return True if the dictionaries meet these conditions and are equal; otherwise, return False.
"""

def compare_dictionaries(dict1, dict2):
    # Check if the number of key-value pairs exceeds the limit
    if len(dict1) > 10 or len(dict2) > 10:
        return False
    
    # Check if all keys are strings and values are positive integers
    for key, value in dict1.items():
        if not isinstance(key, str) or not isinstance(value, int) or value <= 0:
            return False
    
    for key, value in dict2.items():
        if not isinstance(key, str) or not isinstance(value, int) or value <= 0:
            return False
    
    # Check if dictionaries have the same keys and values
    return dict1 == dict2