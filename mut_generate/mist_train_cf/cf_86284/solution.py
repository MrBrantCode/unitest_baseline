"""
QUESTION:
Write a function `find_smallest_number` that takes an array of numbers as input and returns the smallest number in the array. The function should have a time complexity of O(n), where n is the number of elements in the array, and should handle negative numbers, arrays with duplicate numbers, and floating-point numbers. It should not modify the original array or use any additional data structures or arrays.
"""

def find_smallest_number(numbers):
    # Check if the array is empty
    if len(numbers) == 0:
        return None
    
    # Set the initial smallest number as the first element
    smallest = numbers[0]
    
    # Iterate through the rest of the numbers in the array
    for i in range(1, len(numbers)):
        # Update the smallest number if a smaller number is found
        if numbers[i] < smallest:
            smallest = numbers[i]
    
    return smallest