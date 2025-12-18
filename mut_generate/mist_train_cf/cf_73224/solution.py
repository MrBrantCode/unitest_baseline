"""
QUESTION:
Write a function named `check_empty_dict` that takes a dictionary as input and returns True if the dictionary and all its nested dictionaries are empty. If any dictionary is not empty or contains a non-dictionary value, the function should return False. The input dictionary can have multiple levels of nesting.
"""

def check_empty_dict(dictionary):
    if dictionary:
        for key, value in dictionary.items():
            if isinstance(value, dict):
                if not check_empty_dict(value):
                    return False
            else:
                return False
        return True
    else:
        return True