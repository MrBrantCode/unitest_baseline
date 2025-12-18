"""
QUESTION:
Create a function called `filter_primes` that filters out the prime numbers from a given list of integers. The function should return a new list containing only the prime numbers. 

You should implement your own algorithm to determine the primality of each number and handle negative integers by treating them the same as their positive counterparts. The input list will only contain integers and its length will be less than or equal to 1000.
"""

def filter_primes(lst):
    """
    Filters out the prime numbers from a given list of integers.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    list: A new list containing only the prime numbers.
    """
    def is_prime(n):
        """
        Checks if a number is prime.
        
        Args:
        n (int): The number to check.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

    return [n for n in lst if is_prime(abs(n))]