"""
QUESTION:
Write a function named `find_max_difference` that takes an array of integers as input and returns a pair of elements with the greatest difference, where the larger element is located at an index greater than the smaller element. If multiple pairs have the same maximum difference, return the pair with the smallest index of the smaller element. If there are no pairs that satisfy the condition, return an empty array. The function should have a time complexity of O(n).
"""

def find_max_difference(arr):
    min_element = float('inf')
    max_diff = 0
    result = []
    
    for element in arr:
        if element < min_element:
            min_element = element
        elif element - min_element > max_diff:
            max_diff = element - min_element
            result = [min_element, element]
    
    return result