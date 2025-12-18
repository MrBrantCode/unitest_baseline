"""
QUESTION:
Write a function named `find_largest_number` that finds the largest number in a list of integers without using the built-in `max` function and only iterating through the list once. The function should return `None` if the input list is empty.
"""

def find_largest_number(numbers):
    if not numbers:
        return None 
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest