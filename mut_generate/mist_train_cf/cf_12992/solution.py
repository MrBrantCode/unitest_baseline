"""
QUESTION:
Create a function named `combine_dictionaries` that takes two dictionaries as input. The function should return a new dictionary where the keys are the prime numbers present in the input dictionaries, and the corresponding values are the sum of the values from the input dictionaries. The resulting dictionary should exclude keys that have values divisible by 10. The input dictionaries will have positive integers as keys and multiples of 5 as values.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def combine_dictionaries(dict1, dict2):
    """
    Combine two dictionaries, keeping only prime keys with values not divisible by 10.
    
    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
    
    Returns:
        dict: A new dictionary with prime keys and values not divisible by 10.
    """
    result_dict = {}
    for d in [dict1, dict2]:
        for key, value in d.items():
            if is_prime(key) and value % 10 != 0:
                result_dict[key] = result_dict.get(key, 0) + value
    return result_dict