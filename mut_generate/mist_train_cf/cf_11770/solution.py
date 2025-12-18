"""
QUESTION:
Create a function `exclude_vowel_keys` that takes a dictionary as input and returns a new dictionary containing all key-value pairs from the input dictionary except those where the key starts with a vowel (case-insensitive).
"""

def exclude_vowel_keys(input_dict):
    """
    Returns a new dictionary containing all key-value pairs from the input dictionary 
    except those where the key starts with a vowel (case-insensitive).
    
    Parameters:
    input_dict (dict): The input dictionary.
    
    Returns:
    dict: A new dictionary with key-value pairs where the key does not start with a vowel.
    """
    return {key: value for key, value in input_dict.items() if not key[0].lower() in 'aeiou'}