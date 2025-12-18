"""
QUESTION:
Create a function named find_second_largest that takes a list of positive integers as input and returns the second largest value in the list. The function should have a time complexity of O(n), where n is the length of the list. Assume the input list has at least two elements.
"""

def find_second_largest(numbers):
    largest = second_largest = float('-inf')  # Initialize largest and second largest variables to negative infinity
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest