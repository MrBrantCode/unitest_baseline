"""
QUESTION:
Find the second minimum value in an unsorted array of integers using a function named `find_second_minimum` without using built-in sorting functions or data structures. If the array has less than 2 elements, return None. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_second_minimum(nums):
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
    
    return second_min_value