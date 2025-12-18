"""
QUESTION:
Create a function called `multiply_and_filter` that takes a dictionary as input. The function should return a new dictionary with the same keys as the input dictionary, but with the values multiplied by 2. However, only include the keys in the new dictionary if their corresponding values in the input dictionary are both prime numbers and greater than 10.
"""

def multiply_and_filter(dictionary):
    """
    This function filters a dictionary to only include keys with prime values greater than 10, 
    then multiplies these values by 2.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with filtered and multiplied values.
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return {key: value * 2 for key, value in dictionary.items() if value > 10 and is_prime(value)}