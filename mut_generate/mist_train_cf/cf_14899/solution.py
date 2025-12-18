"""
QUESTION:
Create a function named `check_and_sort_list` that takes a list of integers as input and returns the sorted list in ascending order if all numbers in the list are even. If the list contains any odd numbers, return a message indicating that the list contains odd numbers.
"""

def check_and_sort_list(numbers):
    # Check if all numbers are even
    if all(num % 2 == 0 for num in numbers):
        # Sort the list in ascending order
        numbers.sort()
        return numbers
    else:
        return "List contains odd numbers."