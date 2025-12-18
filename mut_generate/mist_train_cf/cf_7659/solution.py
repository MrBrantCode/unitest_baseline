"""
QUESTION:
Write a function `count_primes_and_composites` that takes a list of integers as input, and returns the total count of elements, prime numbers, and composite numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A composite number is a positive integer that has at least one positive divisor other than one or itself. The function should count the numbers correctly, even for large inputs.
"""

import math

def count_primes_and_composites(numbers):
    """
    This function takes a list of integers as input, 
    and returns the total count of elements, prime numbers, and composite numbers in the list.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the total count of elements, prime numbers, and composite numbers.
    """
    total_count = 0
    prime_count = 0
    composite_count = 0

    for num in numbers:
        total_count += 1
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    composite_count += 1
                    break
            else:
                prime_count += 1

    return total_count, prime_count, composite_count