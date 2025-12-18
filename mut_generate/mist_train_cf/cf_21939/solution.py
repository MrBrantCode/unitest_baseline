"""
QUESTION:
Write a function called `power` that calculates the value of a positive integer `x` raised to the power of a positive integer `n`. The function should have a time complexity of O(log n) and should only accept positive integers greater than zero for both `x` and `n`.
"""

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = power(x, n // 2)
        return half_power * half_power
    else:
        half_power = power(x, n // 2)
        return x * half_power * half_power