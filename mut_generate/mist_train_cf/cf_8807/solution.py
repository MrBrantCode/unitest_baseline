"""
QUESTION:
Implement a program with a function `find_prime_factors` that takes an integer `n` as input and returns a tuple containing the smallest prime factor of `n` and the sum of all prime factors of `n`. The function should use recursion to find the prime factors. The program should also include error handling to ensure that the input is a positive integer greater than 1. Additionally, the program should be able to handle multiple inputs and store the results in a data structure, and it should be able to sort the results based on the input numbers. The program should be implemented using object-oriented programming principles.
"""

def find_prime_factors(n):
    """
    This function takes an integer n as input and returns a tuple containing the smallest prime factor of n and the sum of all prime factors of n.
    
    Args:
    n (int): A positive integer greater than 1.
    
    Returns:
    tuple: A tuple containing the smallest prime factor of n and the sum of all prime factors of n.
    """
    
    def find_smallest_prime_factor(n):
        """
        This function finds the smallest prime factor of a given number n.
        
        Args:
        n (int): A positive integer greater than 1.
        
        Returns:
        int: The smallest prime factor of n.
        """
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return i
        return n

    def recursive_prime_factors(n):
        """
        This function finds all prime factors of a given number n using recursion.
        
        Args:
        n (int): A positive integer greater than 1.
        
        Returns:
        list: A list of all prime factors of n.
        """
        smallest_factor = find_smallest_prime_factor(n)
        if smallest_factor == n:
            return [n]
        else:
            return [smallest_factor] + recursive_prime_factors(n // smallest_factor)

    smallest_factor = find_smallest_prime_factor(n)
    factors = recursive_prime_factors(n)
    factors_sum = sum(factors)
    return (smallest_factor, factors_sum)