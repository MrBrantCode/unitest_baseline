"""
QUESTION:
Implement a recursive function `findMin` that takes a list of numbers as input and returns the minimum value from the list. The function should split the list into two halves and recursively call itself on both halves, comparing the minimum values to determine the overall minimum.
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