"""
QUESTION:
Create a function `count_max_occurrences` that takes a 2D array of numerical values as input and returns the number of times the maximum value appears. The function should have a time complexity of O(n^2), where n is the length of the longest row in the 2D array, and use only constant space complexity.
"""

def count_max_occurrences(arr):
    if not arr or not arr[0]:
        return 0
    
    max_value = float('-inf')
    max_count = 0
    
    for row in arr:
        for num in row:
            if num > max_value:
                max_value = num
                max_count = 1
            elif num == max_value:
                max_count += 1
    
    return max_count