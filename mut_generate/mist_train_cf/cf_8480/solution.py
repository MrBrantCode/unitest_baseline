"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of all prime numbers in a given list using only a for loop. The function should take a list of integers as input and return the sum of prime numbers. The function should correctly handle cases where the input list contains non-prime numbers and the number 1, which is not considered prime.
"""

def sum_of_primes(numbers):
    """
    Calculate the sum of all prime numbers in a given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of prime numbers in the list.
    """
    prime_sum = 0

    for num in numbers:
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime and num > 1:  # Exclude 1 from the sum as it is not considered prime
            prime_sum += num

    return prime_sum