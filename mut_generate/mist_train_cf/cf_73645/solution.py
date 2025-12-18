"""
QUESTION:
Develop a generator expression to iterate through a provided sequence of whole numbers and yield only the prime numbers. 

The function should take a sequence of integers as input and exclude non-prime entities from the output. Use a helper function `is_prime(n)` to check whether a number is prime.
"""

def get_primes(sequence):
    """
    A generator function to iterate through a sequence of whole numbers and yield only the prime numbers.
    """
    def is_prime(n):
        """
        A helper function to determine whether a given number is prime.
        """
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
    
    return (num for num in sequence if is_prime(num))