"""
QUESTION:
Design a function `ternary_search_jagged_array` that performs a ternary search on a jagged array. The function should take two parameters: a 2D jagged array where each sub-array is sorted and a target value. It should return `True` if the target value is found in the jagged array and `False` otherwise. The function should work efficiently by dividing each sub-array into three parts and searching for the target value.
"""

def ternary_search_jagged_array(jagged_array, target):
    for row in jagged_array:
        left = 0    
        right = len(row)-1 
        while left <= right:
            partition_size = (right-left) // 3 
            mid1 = left + partition_size    
            mid2 = right - partition_size
            if mid1<len(row) and row[mid1] == target:
                return True
            if mid2<len(row) and row[mid2] == target:
                return True
            if mid1<len(row) and row[mid1] < target:                 
                left = mid1 + 1
            elif mid2<len(row) and row[mid2] > target:        
                right = mid2 - 1
            else:        
                left = mid1 + 1
                right = mid2 - 1
    return False