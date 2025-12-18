"""
QUESTION:
Write a function `find_max_value_range` that takes a list of integers `lst` and a range `rng` as input. The function should return the maximum prime number in the list within the given range, provided that the minimum value within the range is divisible by 3 and the maximum value is greater than the minimum value. If no such value exists, the function should return `None`. The time complexity of the function should be O(n), where n is the number of elements in the list.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_max_value_range(lst, rng):
    min_val = float('inf')
    max_val = float('-inf')

    for num in lst:
        if num >= rng[0] and num <= rng[1]:
            if num < min_val and num % 3 == 0:
                min_val = num
            if num > max_val and is_prime(num):
                max_val = num

    return max_val if max_val > min_val else None