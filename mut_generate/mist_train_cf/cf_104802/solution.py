"""
QUESTION:
Write a function named `correct_solution` that takes a list of numbers as input, removes all negative numbers, doubles the remaining numbers, and returns the doubled numbers in descending order. The function should not modify the original list.
"""

def correct_solution(numbers):
    filtered_numbers = [num for num in numbers if num >= 0]
    doubled_numbers = [num * 2 for num in filtered_numbers]
    sorted_numbers = sorted(doubled_numbers, reverse=True)
    return sorted_numbers