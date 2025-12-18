"""
QUESTION:
Find and return the two largest unique numbers in the input array of integers. The output should be in descending order. If there are fewer than two unique numbers in the array, return an empty array. The input array can have duplicate numbers and both positive and negative numbers. Implement this function in Python as `find_two_largest_unique(numbers)`.
"""

def find_two_largest_unique(numbers):
    max1 = float('-inf')
    max2 = float('-inf')
    
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num < max1 and num > max2:
            max2 = num
    
    result = []
    
    if max2 == float('-inf'):
        return result
    
    result.append(max1)
    result.append(max2)
    return result