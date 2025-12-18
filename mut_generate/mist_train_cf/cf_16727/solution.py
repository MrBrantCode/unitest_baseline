"""
QUESTION:
Create a function called `sum_of_primes` that generates a list of prime numbers up to a given integer `n` and returns their sum. The function should only include prime numbers in the list and the list should be in descending order, but the sum is the actual output, not the list.
"""

def sum_of_primes(n):
    """
    Generates a list of prime numbers up to a given integer n and returns their sum.
    
    Args:
    n (int): The upper limit for generating prime numbers.
    
    Returns:
    int: The sum of prime numbers up to n.
    """
    def is_prime(num):
        """
        Checks if a number is prime.
        
        Args:
        num (int): The number to check.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return sum(primes)