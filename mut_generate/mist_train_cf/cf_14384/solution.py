"""
QUESTION:
Write a function called `calculate_largest_number` that takes a list of integers as input and returns the largest number in the list, considering both positive and negative integers, as well as duplicates. The input list may contain any number of elements, including zero. The function should return the maximum number present in the list.
"""

def calculate_largest_number(numbers):
    max_number = float('-inf')  # initialize max_number with negative infinity
    unique_numbers = set(numbers)  # get unique numbers using a set

    for number in unique_numbers:
        if number > max_number:  # update max_number if current number is greater
            max_number = number

    return max_number