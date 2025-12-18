"""
QUESTION:
Create a function `generate_pattern_and_check_prime` that generates an array of size 10 with elements following a specific pattern, where the first element is 1 and each subsequent element is the previous element raised to the power of its 1-based index. Additionally, create a boolean array of the same size where each element indicates whether the corresponding element in the first array is prime or not.
"""

import math

def generate_pattern_and_check_prime(size=10):
    """
    Generates an array of size 'size' with elements following a specific pattern,
    where the first element is 1 and each subsequent element is the previous
    element raised to the power of its 1-based index. Additionally, creates a
    boolean array of the same size where each element indicates whether the
    corresponding element in the first array is prime or not.

    Args:
        size (int): The size of the array. Defaults to 10.

    Returns:
        tuple: A tuple containing two arrays, the first with the pattern and
            the second with the primality of each element.
    """
    numbers = [0] * size
    is_prime = [False] * size

    # Assign elements in the specified pattern
    numbers[0] = 1
    for i in range(1, size):
        numbers[i] = numbers[i-1] ** (i+1)

    # Check if each element is prime
    for i in range(size):
        if numbers[i] < 2:
            is_prime[i] = False
        else:
            is_prime[i] = True
            for j in range(2, int(math.sqrt(numbers[i])) + 1):
                if numbers[i] % j == 0:
                    is_prime[i] = False
                    break

    return numbers, is_prime