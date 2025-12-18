"""
QUESTION:
Write a function `sum_and_average_odd_elements` that takes a list of integers as input and returns the average of all odd elements in the list. The function should not use built-in functions to calculate the sum or average, and it should not use the modulus operator (%) to check if a number is odd. The input list will have at least 1000 elements.
"""

def sum_and_average_odd_elements(lst):
    odd_sum = 0
    odd_count = 0

    for num in lst:
        odd_sum += num * (num & 1)  # multiply by 1 if odd, 0 if even
        odd_count += num & 1  # count 1 if odd, 0 if even

    average = odd_sum / odd_count if odd_count != 0 else 0
    return average