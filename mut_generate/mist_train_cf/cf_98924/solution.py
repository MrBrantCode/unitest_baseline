"""
QUESTION:
Create a function called `find_second_smallest` that takes a list of integers as input and returns the second smallest number in the list without using any built-in functions or libraries. The function should handle duplicates and return the second smallest number. The input list will be provided as an argument to the function.
"""

def find_second_smallest(numbers):
    smallest = float('inf')
    second_smallest = float('inf')
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest