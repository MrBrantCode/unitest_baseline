"""
QUESTION:
Create a function `count_squared_values` that takes a list of integers as input. The function should iterate over each number in the list, square it, and check if the squared value is divisible by 3. Additionally, it should check if the square root of the squared value is a prime number and if the sum of the digits in the squared value is less than or equal to 10. If a squared value meets all these conditions, print the squared value and increment a counter. The function should return the total count of squared values meeting all conditions. The input list should not be modified.
"""

import math

def count_squared_values(nums):
    """
    This function takes a list of integers, squares each number, and checks if the squared value is divisible by 3.
    It also checks if the square root of the squared value is a prime number and if the sum of the digits in the squared value is less than or equal to 10.
    If a squared value meets all these conditions, it prints the squared value and increments a counter.
    The function returns the total count of squared values meeting all conditions.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The total count of squared values meeting all conditions.
    """

    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in nums:
        squared_value = num ** 2
        if squared_value % 3 == 0 and is_prime(math.isqrt(squared_value)):
            digit_sum = sum(int(digit) for digit in str(squared_value))
            if digit_sum <= 10:
                print(squared_value)
                count += 1
    return count