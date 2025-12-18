"""
QUESTION:
Create a function called `calculate_sum` that uses the reduce function to calculate the sum of numbers in an array, following these conditions:

- Numbers are positive integers ranging from 1 to 100.
- Numbers divisible by both 3 and 5 should be subtracted by one-third of their value from the sum.
- Numbers divisible by 7 should be multiplied by 2 before adding to the sum.
- Numbers divisible by either 3 or 5 but not both should add half of their value to the sum.
- The final sum should be rounded to the nearest hundredth.
"""

import math
from functools import reduce

def calculate_sum(numbers):
    def helper(acc, num):
        if num % 3 == 0 and num % 5 == 0:  # divisible by both 3 and 5
            acc -= num / 3
        elif num % 7 == 0:  # divisible by 7
            acc += num * 2
        elif num % 3 == 0 or num % 5 == 0:  # divisible by either 3 or 5 but not both
            acc += num / 2
        else:
            acc += num
        return acc

    return round(reduce(helper, numbers, 0), 2)