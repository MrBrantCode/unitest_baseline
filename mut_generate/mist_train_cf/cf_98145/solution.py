"""
QUESTION:
Write a function `multiply_numbers(numbers, multipliers)` that takes two lists of integers, `numbers` and `multipliers`, and returns the sum of the products of corresponding elements from the two lists. The function should iterate over both lists simultaneously, multiplying each element from `numbers` with the corresponding element from `multipliers` and adding the product to the running total. The function should return the final sum.
"""

def multiply_numbers(numbers, multipliers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i] * multipliers[i]
    return result