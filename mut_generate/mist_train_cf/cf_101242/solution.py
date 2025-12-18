"""
QUESTION:
Write a function named `sum_of_even_numbers` that takes an integer `n` as input and returns the sum of all even numbers from 2 to `n`, the list of even numbers used in the calculation, and the count of these even numbers. The function should achieve this in O(log n) time complexity.
"""

def sum_of_even_numbers(n):
    even_numbers = [i for i in range(2, n + 1, 2)]
    even_sum = sum(even_numbers)
    count = len(even_numbers)
    index = len(even_numbers) - 1
    used_numbers = even_numbers[:index+1]
    used_count = len(used_numbers)
    return even_sum, used_numbers, used_count