"""
QUESTION:
Write a function `filter_and_sum` that takes a list of integers as input, filters out numbers that are less than or equal to 100 or greater than or equal to 1000, sorts the remaining numbers in descending order, and returns the sum of their square roots with an accuracy of at least 10 decimal places. The time complexity should be O(n log n) and space complexity should be O(n), where n is the length of the list. The input list can contain up to 10^6 elements.
"""

import math

def filter_and_sum(numbers):
    filtered_numbers = []
    for num in numbers:
        if 100 < num < 1000:
            filtered_numbers.append(num)
    
    filtered_numbers.sort(reverse=True)
    
    sum_of_square_roots = 0
    for num in filtered_numbers:
        sum_of_square_roots += math.sqrt(num)
    
    return round(sum_of_square_roots, 10)