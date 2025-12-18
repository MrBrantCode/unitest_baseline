"""
QUESTION:
Write a function `find_second_largest` that takes an array of at least 2 unique integers as input and returns the element with the second greatest value. The function should not use any built-in sorting functions or methods and must have a time complexity of O(n), where n is the length of the array.
"""

def find_second_largest(numbers):
    # Initialize variables to keep track of the largest and second largest values
    largest = float('-inf')
    second_largest = float('-inf')

    # Iterate through the array
    for num in numbers:
        # If the current number is larger than the largest value, update the largest and second largest values
        if num > largest:
            second_largest = largest
            largest = num
        # If the current number is between the largest and second largest values, update the second largest value
        elif num > second_largest and num < largest:
            second_largest = num

    return second_largest