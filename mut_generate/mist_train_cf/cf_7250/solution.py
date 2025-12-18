"""
QUESTION:
Create a function `create_prime_cube_root_dict()` that generates a dictionary with prime numbers less than 20 as keys and their corresponding cube roots as values. The dictionary should be ordered such that both keys and values are in ascending order. Implement error handling to address any potential exceptions during dictionary creation.
"""

import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def create_prime_cube_root_dict():
    """
    Generates a dictionary with prime numbers less than 20 as keys and their corresponding cube roots as values.
    
    The dictionary is ordered such that both keys and values are in ascending order.
    
    Returns:
        dict: A dictionary with prime numbers as keys and their cube roots as values.
    
    Raises:
        Exception: If any error occurs during dictionary creation.
    """
    try:
        prime_cube_root_dict = {}
        for num in range(2, 20):
            if is_prime(num):
                prime_cube_root_dict[num] = round(num ** (1/3), 4)
        # Sort the dictionary by keys and then by values
        sorted_dict = dict(sorted(prime_cube_root_dict.items(), key=lambda item: (item[0], item[1])))
        return sorted_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return None