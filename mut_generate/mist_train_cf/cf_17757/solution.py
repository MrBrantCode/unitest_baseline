"""
QUESTION:
Write a function `find_max` that takes an array of integers as input and returns the maximum value in the array, following these rules:
- If the array is empty, return None.
- If the array contains duplicate maximum values, return the last occurrence of the maximum value.
- If the array contains only negative values, return the maximum negative value with a time complexity of O(nlogn).
- If the array contains both positive and negative values, return the maximum positive value with a space complexity of O(1).
- If the array contains only zero values, return zero.
"""

def find_max(input_array):
    # Condition 1: If the array is empty, return None
    if len(input_array) == 0:
        return None
    
    # Condition 2: If the array contains duplicate maximum values, return the last occurrence
    max_val = float('-inf')
    max_index = -1
    for i in range(len(input_array)):
        if input_array[i] >= max_val:
            max_val = input_array[i]
            max_index = i
    
    # Condition 3: If the array contains only negative values, return the maximum negative value
    if max_val < 0:
        sorted_array = sorted(input_array)
        return sorted_array[-1]
    
    # Condition 4: If the array contains both positive and negative values, return the maximum positive value
    max_positive = float('-inf')
    for num in input_array:
        if num > max_positive:
            max_positive = num
    
    # Condition 5: If the array contains only zero values, return zero
    if max_positive == float('-inf'):
        return 0
    
    return max_positive