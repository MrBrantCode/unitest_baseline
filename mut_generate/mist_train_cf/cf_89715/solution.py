"""
QUESTION:
Create a function named `get_prime_numbers` that takes two parameters, `start` and `end`, and returns a list of unique prime numbers between the `start` and `end` values (inclusive). The function should handle negative numbers as inputs and validate that `start` is less than or equal to `end`. If the inputs are not valid, the function should return an empty list.
"""

def get_prime_numbers(start, end):
    """
    Returns a list of unique prime numbers between the start and end values (inclusive).
    
    Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).
    
    Returns:
    list: A list of unique prime numbers between start and end.
    """
    
    if start > end:
        return []
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in range(start, end + 1) if is_prime(abs(num))]
    
    return list(set(primes))