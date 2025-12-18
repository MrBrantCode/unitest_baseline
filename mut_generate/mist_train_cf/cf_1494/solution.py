"""
QUESTION:
Write a function named `sum_primes` to calculate the sum of all prime numbers from 2 to 10. The function should not use any built-in functions or libraries to check if a number is prime. The function should return the sum of prime numbers.
"""

def sum_primes(n):
    """
    Calculate the sum of all prime numbers from 2 to n.
    
    Args:
    n (int): The upper limit for the prime number range.
    
    Returns:
    int: The sum of prime numbers from 2 to n.
    """
    sum_prime = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break
        if is_prime:
            sum_prime += i
    return sum_prime