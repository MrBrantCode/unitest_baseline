"""
QUESTION:
Write a function called `find_lucid_numbers` that takes an integer `n` as input and returns all numbers less than or equal to `n` that are divisible by the sum of their digits.
"""

def find_lucid_numbers(n):
    lucid_numbers = []
    for i in range(1, n+1):
        sum_of_digits = sum(int(digit) for digit in str(i))
        if i % sum_of_digits == 0:
            lucid_numbers.append(i)
    return lucid_numbers