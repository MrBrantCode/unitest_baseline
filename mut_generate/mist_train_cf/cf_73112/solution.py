"""
QUESTION:
Create a function `is_perfect(n)` that takes an integer `n` as input and returns a boolean value indicating whether `n` is a perfect number. A perfect number is a positive integer that is equal to the sum of its positive divisors excluding the number itself. The function should also be able to handle inputs less than 1 and return False. Additionally, create a function `check_numbers(numbers)` that takes a list of integers as input and returns a list of boolean values corresponding to each input using the `is_perfect(n)` function. The function should optimize its performance by only checking for divisors up to the square root of `n`.
"""

import math

def entrance(n):
    if n < 1:
        return False

    sum = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            if i == n/i:
                sum = sum + i
            else:
                sum = sum + i + n/i

    return sum == n