"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of all prime numbers between 0 and a given upper limit. The function should iterate over each number in the range, check if it's prime, and add it to the sum if it is. The function should return the sum of prime numbers. The input will be an integer and the output should also be an integer. The function should not take any arguments other than the upper limit.
"""

import math

def sum_of_primes(n):
    """
    This function calculates the sum of all prime numbers between 0 and a given upper limit.

    Args:
    n (int): The upper limit.

    Returns:
    int: The sum of prime numbers.
    """
    sum = 0
    for num in range(0, n + 1):
        if num == 2:
            sum += num
        elif num > 2:
            is_prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                sum += num
    return sum