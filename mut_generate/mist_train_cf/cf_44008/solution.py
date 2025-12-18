"""
QUESTION:
Write a function named `second_largest` that takes a list of numbers as input and returns the second largest number in the list. The function should handle cases where there may not be a second largest number (e.g., if the list has less than two distinct elements). Assume that the input list contains only integers and has at least one element.
"""

def entrance(numbers):
    # Initialize two variables, one for the largest number and one for the second largest
    first, second = float('-inf'), float('-inf')
    # Iterate over each number in the list
    for num in numbers:
        # If the current number is greater than the largest number, update first and second
        if num > first:
            first, second = num, first
        # If the current number is between first and second, update second
        elif first > num > second:
            second = num
    return second