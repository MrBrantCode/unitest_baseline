"""
QUESTION:
Write a function `sum_of_even_numbers` that takes in two parameters: a positive integer `max_number` and a positive integer `step_size`, both of which are less than or equal to 10^9 and 1000, respectively. The function should return the sum of all even numbers between 0 and `max_number` (inclusive) where each even number is incremented by the `step_size`, and should have a time complexity of O(1).
"""

def sum_of_even_numbers(max_number, step_size):
    last_term = ((max_number // 2) * 2)
    number_of_terms = (last_term // (step_size * 2)) + 1
    sum_of_series = number_of_terms / 2 * (0 + last_term)
    return sum_of_series