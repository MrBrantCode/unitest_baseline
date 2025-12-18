"""
QUESTION:
Write a function called `find_odd_numbers` that takes two positive integers `n` and `m` as parameters. The function should return a list of all odd numbers from `n` to `m` (not including `m`). It is required that `n` is less than `m`. If this condition is not met, the function should return an error message indicating that `n` should be less than `m`.
"""

def find_odd_numbers(n, m):
    if n < m:
        return [num for num in range(n, m) if num % 2 != 0]
    else:
        return "n should be less than m"