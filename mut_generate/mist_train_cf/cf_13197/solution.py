"""
QUESTION:
Write a function `find_largest_prime` that takes a list of numbers as input and returns the largest prime number in the list. The list may contain integers and floats, but the function should only consider integers. If no prime number is found, the function should return None.
"""

def find_largest_prime(numbers):
    """
    This function finds the largest prime number in a list of numbers.
    
    Parameters:
    numbers (list): A list containing integers and/or floats.
    
    Returns:
    int or None: The largest prime number in the list, or None if no prime number is found.
    """
    
    # Filter out non-integer values
    numbers = [num for num in numbers if isinstance(num, int)]
    
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # Find the largest prime number
    largest_prime = max((num for num in numbers if is_prime(num)), default=None)
    
    return largest_prime