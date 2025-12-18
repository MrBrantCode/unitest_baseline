"""
QUESTION:
Create a function `create_mapping(dictionary)` that takes a dictionary as input and returns a new dictionary where all keys are uppercase, all values are positive integers, and only keys starting with a vowel are included. The function should also ensure that the sum of all values in the resulting dictionary is a prime number. If the sum is not a prime number, return an empty dictionary.
"""

def create_mapping(dictionary):
    """
    Create a new dictionary where all keys are uppercase, all values are positive integers, 
    and only keys starting with a vowel are included. The function also ensures that the 
    sum of all values in the resulting dictionary is a prime number. If the sum is not a 
    prime number, return an empty dictionary.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with the specified properties.
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}
    mapped_dict = {}
    sum_values = 0

    for key, value in dictionary.items():
        if key.lower()[0] in vowels:
            if isinstance(value, int) and value > 0:
                mapped_dict[key.upper()] = value
        if isinstance(value, int) and value > 0:
            sum_values += value

    def is_prime(n):
        """
        Helper function to check if a number is prime.

        Args:
            n (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(sum_values):
        return mapped_dict
    else:
        return {}