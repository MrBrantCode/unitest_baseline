"""
QUESTION:
_Based on [Project Euler problem 35](https://projecteuler.net/problem=35)_

A circular prime is a prime in which every circular permutation of that number is also prime. Circular permutations are created by rotating the digits of the number, for example: `197, 971, 719`. One-digit primes are circular primes by definition.

Complete the function that dertermines if a number is a circular prime.

There are 100 random tests for numbers up to 10000.
"""

def is_circular_prime(n: int) -> bool:
    """
    Determines if a given number is a circular prime.

    A circular prime is a prime number where all of its circular permutations
    are also prime numbers.

    Parameters:
    n (int): The number to be checked.

    Returns:
    bool: True if the number is a circular prime, False otherwise.
    """
    
    def circular_permutations(n: int) -> list[int]:
        """
        Generates all circular permutations of a given number.

        Parameters:
        n (int): The number to generate permutations for.

        Returns:
        list[int]: A list of all circular permutations of the number.
        """
        n_str = str(n)
        return [int(n_str[i:] + n_str[:i]) for i in range(len(n_str))]
    
    def is_prime(n: int) -> bool:
        """
        Checks if a given number is a prime number.

        Parameters:
        n (int): The number to be checked.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Generate all circular permutations of the number
    permutations = circular_permutations(n)
    
    # Check if all permutations are prime
    return all(is_prime(p) for p in permutations)