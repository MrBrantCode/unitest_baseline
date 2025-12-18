"""
QUESTION:
Write a function `find_largest_smallest` that takes a list of integers as input and returns the largest and smallest numbers in the list. The function should be able to handle a list of any size, but assume that the list will not be empty.
"""

def find_largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest