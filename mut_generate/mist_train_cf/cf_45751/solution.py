"""
QUESTION:
Write a function called `unique_sum_mult_powers` that takes a list of integers `arr` as input. The function should return the sum of each unique integer in `arr` raised to its absolute value, multiplied by the number of unique integers in `arr`. If `arr` is empty, the function should return `None`.
"""

def unique_sum_mult_powers(arr):
    if not arr:
        return None
    unique_elements = list(set(arr))
    cum_sum = 0
    for el in unique_elements:
        cum_sum += el ** abs(el)
    return cum_sum * len(unique_elements)