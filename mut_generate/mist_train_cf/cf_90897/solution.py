"""
QUESTION:
Implement a function called `findMin` that recursively calculates the minimum value in a list of numbers. The function should take a list of numbers as input and return the smallest number in the list.
"""

def findMin(numbers):
    # Base case: list contains only one number
    if len(numbers) == 1:
        return numbers[0]
    
    # Split the list into two halves
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    
    # Recursive calls
    left_min = findMin(left_half)
    right_min = findMin(right_half)
    
    # Return the smaller minimum value
    return min(left_min, right_min)