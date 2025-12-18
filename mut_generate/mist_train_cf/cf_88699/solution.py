"""
QUESTION:
Write a function `sum_of_even_numbers` that takes two parameters: `max_number` and `step_size`, both positive integers. The function should return the sum of all even numbers between 0 and `max_number` (inclusive) where each even number is incremented by `step_size`. The function should have a time complexity of O(1).
"""

def sum_of_even_numbers(max_number, step_size):
    last_term = ((max_number // 2) * 2)
    number_of_terms = (last_term // step_size) + 1
    sum_of_series = number_of_terms / 2 * (0 + last_term)
    return sum_of_series