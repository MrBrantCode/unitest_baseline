"""
QUESTION:
Create a function named `get_prime_numbers` that takes a list of integers as input. The function should first remove any duplicates from the list. Then, it should filter out non-prime numbers and return a new list containing only the prime numbers from the original list.
"""

def get_prime_numbers(numbers):
    """
    This function takes a list of integers, removes duplicates, 
    filters out non-prime numbers and returns a list of prime numbers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    list: A list of prime numbers.
    """
    
    # Remove duplicates by converting the list to a set
    unique_numbers = set(numbers)
    
    # Define a helper function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Filter out non-prime numbers
    prime_numbers = [num for num in unique_numbers if is_prime(num)]
    
    return prime_numbers