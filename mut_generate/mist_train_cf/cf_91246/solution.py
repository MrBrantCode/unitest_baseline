"""
QUESTION:
Write a function called `find_largest_smallest` that takes a list of integers as input and returns the largest and smallest numbers in the list. The function must run in O(n) time complexity, where n is the size of the input list, and must not use any built-in functions or libraries to find the largest and smallest numbers. The function must also handle edge cases, such as an empty list or a list with only one element.
"""

def find_largest_smallest(numbers):
    if len(numbers) == 0:
        return None, None
    elif len(numbers) == 1:
        return numbers[0], numbers[0]

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest