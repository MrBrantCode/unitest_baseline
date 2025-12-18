"""
QUESTION:
Write a function called `find_max_difference` that takes an array of integers as input and returns the maximum difference between a lower element and an upper element, where the lower element must come before the upper element in the array. The function must have a time complexity of O(n) and a space complexity of O(1), and it must not use any built-in sorting functions or data structures. The function should handle negative integers in the array as well.
"""

def find_max_difference(arr):
    min_value = arr[0]
    max_diff = 0
    
    for num in arr:
        if num < min_value:
            min_value = num
        elif num - min_value > max_diff:
            max_diff = num - min_value
            
    return max_diff