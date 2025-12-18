"""
QUESTION:
Create a function named `cumulative_sum_positive` that takes a list of integers as input and returns a list of integers. The output list should contain the cumulative sum of only the positive numbers in the input list, ignoring any negative numbers.
"""

def cumulative_sum_positive(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    cumulative_sum = []
    current_sum = 0
    for num in positive_numbers:
        current_sum += num
        cumulative_sum.append(current_sum)
    return cumulative_sum