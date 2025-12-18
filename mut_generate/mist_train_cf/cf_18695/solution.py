"""
QUESTION:
Implement the `calculate_difference` function that takes two numbers `num1` and `num2` as parameters. The function should return the difference between `num1` and `num2` under the following conditions:

- The difference should only be calculated if `num1` is larger than `num2`. If `num1` is smaller or equal to `num2`, return the message "The difference cannot be calculated."
- If `num1` is a prime number, the difference should be calculated using the absolute values of `num1` and `num2`. Otherwise, the difference should be calculated using the negative difference of `num1` and `num2`.
- If the calculated difference can be evenly divided by 2, return the result divided by 2. Otherwise, return the result multiplied by 2.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def calculate_difference(num1, num2):
    if num1 <= num2:
        return "The difference cannot be calculated."

    if is_prime(num1):
        difference = abs(num1 - num2)
    else:
        difference = -(num1 - num2)

    if difference % 2 == 0:
        return difference // 2
    else:
        return difference * 2