"""
QUESTION:
Write a function named `find_max_value_in_range` that takes a list of integers and a range as input, and returns the maximum value within the range that is a prime number and a perfect square. The function should also consider the minimum value within the range that is divisible by 3 and 2, and a perfect cube. The function should return the maximum value only if it is greater than the minimum value. The function should run in O(n) time complexity.
"""

import math

def find_max_value_in_range(lst, range_start, range_end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect_square(n):
        sqrt = int(math.sqrt(n))
        return sqrt * sqrt == n

    def is_perfect_cube(n):
        cbrt = int(round(n ** (1/3)))
        return cbrt * cbrt * cbrt == n

    max_value = float('-inf')
    min_value = float('inf')

    for num in lst:
        if range_start <= num <= range_end:
            if num > max_value and is_prime(num) and is_perfect_square(num):
                max_value = num
            if num < min_value and num % 3 == 0 and num % 2 == 0 and is_perfect_cube(num):
                min_value = num

    if max_value > min_value:
        return max_value
    else:
        return None