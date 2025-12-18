"""
QUESTION:
Create a function called `filter_prime_numbers` that takes a list of integers as input and returns a new list containing only prime numbers greater than 5 and less than 10. The number 6 should be excluded from the output.
"""

def filter_prime_numbers(numbers):
    """
    This function filters a list of integers and returns a new list containing only prime numbers greater than 5 and less than 10, excluding 6.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        list: A list of prime numbers greater than 5 and less than 10, excluding 6.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num) and 5 < num < 10 and num != 6]