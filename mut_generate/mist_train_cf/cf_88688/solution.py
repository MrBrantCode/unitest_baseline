"""
QUESTION:
Write a recursive function named `reverse_list` to reverse a list of at least 10 numbers. The function must not use any built-in functions or methods to reverse the list. If the input list is empty, it should return the original list.
"""

def reverse_list(numbers):
    if len(numbers) <= 1:
        return numbers
    return [numbers[-1]] + reverse_list(numbers[:-1])