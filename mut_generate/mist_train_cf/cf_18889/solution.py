"""
QUESTION:
Write a function named `squared_values` that iterates over a list of integers and prints the squared values that are divisible by 3 and have a prime square root. The function should also return the total count of squared values that meet these conditions.
"""

import math

def squared_values(nums):
    """
    This function iterates over a list of integers, prints the squared values that are divisible by 3 and have a prime square root, 
    and returns the total count of such squared values.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The total count of squared values that meet the conditions.
    """
    count = 0
    for num in nums:
        if num ** 2 % 3 == 0 and math.isqrt(num ** 2) > 1:
            is_prime = True
            for i in range(2, math.isqrt(num ** 2)):
                if (num ** 2) % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num ** 2)
                count += 1
    return count