"""
QUESTION:
Write a function `filter_and_sort` that takes an array of numbers as input, filters the numbers that are divisible by 3, squares them, removes duplicates, sorts them in descending order, and returns the first 5 numbers. The function should not include any input validation or error checking.
"""

def filter_and_sort(numbers):
    divisible_by_3_array = [num ** 2 for num in numbers if num % 3 == 0]
    unique_array = sorted(set(divisible_by_3_array), reverse=True)
    return unique_array[:5]