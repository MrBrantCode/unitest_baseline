"""
QUESTION:
Write a function `sum_unique_elements` that takes a list of positive integers as input, calculates the sum of unique elements that are greater than 0, less than or equal to 100, and divisible by 5, and returns the sum. The function should handle lists with up to 1 million elements.
"""

def sum_unique_elements(lst):
    unique_elements = set()
    total_sum = 0

    for element in lst:
        if 0 < element <= 100 and element % 5 == 0:
            if element not in unique_elements:
                total_sum += element
                unique_elements.add(element)

    return total_sum