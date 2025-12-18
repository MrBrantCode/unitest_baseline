"""
QUESTION:
Write a function named `find_second_largest` that takes a list of integers as input and returns the second largest element. The function should be able to handle a list with duplicate elements and should return the second largest unique element. If there is no second largest element (i.e., if all elements in the list are the same), the function should return the smallest possible integer value. The list can contain both positive and negative integers.
"""

def find_second_largest(numbers):
    # Initialize the largest and second_largest variables
    largest = float('-inf')
    second_largest = float('-inf')
    
    # Iterate over each number in the list
    for num in numbers:
        # If the current number is greater than the largest, update both largest and second_largest
        if num > largest:
            second_largest = largest
            largest = num
        # If the current number is between largest and second_largest, update only second_largest
        elif num > second_largest and num != largest:
            second_largest = num
    
    # Return the second_largest element
    return second_largest