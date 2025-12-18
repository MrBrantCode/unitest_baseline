"""
QUESTION:
Write a function named `calculate_median` that takes a list of numbers as input and returns the median of the list. The function should handle both odd and even number of inputs. The input list is not guaranteed to be sorted.
"""

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle_index = n // 2
    
    if n % 2 == 1:  # odd number of elements
        median = sorted_numbers[middle_index]
    else:  # even number of elements
        median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    
    return median