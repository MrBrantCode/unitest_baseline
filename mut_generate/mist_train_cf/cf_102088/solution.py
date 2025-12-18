"""
QUESTION:
Write a function `find_largest_smallest` that takes a list of integers as input and returns the smallest and largest numbers in the list. The function should have a time complexity of O(n), handle edge cases, and not use any built-in functions or libraries to find the largest and smallest numbers.
"""

def find_largest_smallest(numbers):
    if len(numbers) == 0:
        return None, None
    if len(numbers) == 1:
        return numbers[0], numbers[0]

    largest = smallest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return smallest, largest