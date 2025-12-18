"""
QUESTION:
Write a function called `calculate_power` that takes two parameters, `n` and `m`, where `n` is a number that can be either an integer or a float, and `m` is an integer exponent. 

The function must handle the following edge cases: 
- If `n` is negative and `m` is not an integer, return "Error: Invalid input, m must be an integer."
- If `n` is zero and `m` is negative, return "Error: Invalid input, n must be non-zero for negative exponent."
- If either `n` or `m` is greater than 1000, use a more efficient algorithm to calculate the power. If `n` is negative and `m` is greater than 1000, use a different efficient algorithm.
- If `n` is a floating-point number and `m` is an integer, round the result to the nearest integer.

The function should have a time complexity of O(log(m)) and a space complexity of O(1).
"""

from typing import Union

def calculate_power(n: Union[int, float], m: int) -> Union[int, float, str]:
    if n < 0 and not isinstance(m, int):
        return "Error: Invalid input, m must be an integer"
    if n == 0 and m < 0:
        return "Error: Invalid input, n must be non-zero for negative exponent"

    if n > 1000 or m > 1000:
        if n < 0:
            result = 1
            while m > 0:
                if m % 2 == 1:
                    result /= n
                n *= n
                m //= 2
        else:
            result = 1
            while m > 0:
                if m % 2 == 1:
                    result *= n
                n *= n
                m //= 2
    else:
        result = 1
        if m > 0:
            for _ in range(m):
                result *= n
        else:
            for _ in range(-m):
                result /= n

    if isinstance(n, float) and isinstance(m, int):
        result = round(result)
    
    return result