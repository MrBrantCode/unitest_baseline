"""
QUESTION:
Implement a function `find_second_minimum(nums)` that finds the second minimum value in an unsorted array of integers without using any built-in sorting functions or data structures. The input array `nums` contains at least one element, and the function should return the second minimum value if it exists; otherwise, it should return a value indicating that the second minimum does not exist. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def entance(nums):
    if len(nums) < 2:
        return None
    
    min_value = float('inf')
    second_min_value = float('inf')
    
    for num in nums:
        if num < min_value:
            second_min_value = min_value
            min_value = num
        elif num < second_min_value and num != min_value:
            second_min_value = num
    
    return second_min_value if second_min_value != float('inf') else None