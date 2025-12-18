"""
QUESTION:
Write a function called `find_second_largest` that takes a list of integers as input and returns the second largest distinct number. If there is no second largest distinct number, return -1. The input list can contain duplicates, but the second largest number should be distinct.
"""

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates from the list
    if len(unique_numbers) < 2:  # If there are less than 2 distinct numbers
        return -1
    else:
        unique_numbers.sort()  # Sort the list in ascending order
        return unique_numbers[-2]  # Return the second largest number