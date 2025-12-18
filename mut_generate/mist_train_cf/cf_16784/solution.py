"""
QUESTION:
Write a function `find_largest_and_smallest` that takes a list of integers as input and returns the largest and smallest numbers in the list. The function should have a time complexity of O(n), where n is the size of the input list, and should not use any built-in functions or libraries to find the largest and smallest numbers. The function should also handle edge cases such as an empty list or a list with only one element, as well as duplicate numbers in the list.
"""

def find_largest_and_smallest(numbers):
    if not numbers:  # Check if the list is empty
        return None, None

    largest = smallest = numbers[0]  # Initialize largest and smallest to the first element

    for number in numbers:
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number

    return largest, smallest