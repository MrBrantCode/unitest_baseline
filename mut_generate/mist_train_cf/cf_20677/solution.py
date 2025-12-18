"""
QUESTION:
Write a recursive function `sum_odd_numbers(n)` that returns the sum of all odd numbers up to the given number `n`, excluding any multiples of 3. The function should handle the base case where `n` is 1 and recursively sum odd numbers that are not multiples of 3.
"""

def entance(n):
    # Base case: if n is 1, return 1 (the only odd number less than or equal to 1)
    if n == 1:
        return 1
    # Recursive case: if n is odd and not a multiple of 3, add it to the sum
    if n % 2 == 1 and n % 3 != 0:
        return n + entance(n - 1)
    # Recursive case: if n is even or a multiple of 3, skip it and move to the next number
    else:
        return entance(n - 1)