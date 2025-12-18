"""
QUESTION:
Write a function `filter_even_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the input list. The function should use a single loop and have a time complexity of O(n), where n is the length of the input list.
"""

def filter_even_numbers(numbers):
    filtered_numbers = []
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)
    return filtered_numbers