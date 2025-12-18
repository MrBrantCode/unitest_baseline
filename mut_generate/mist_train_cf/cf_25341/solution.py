"""
QUESTION:
Write a function called `find_max_element` that takes an array of integers as input and returns the maximum element. The function should have a time complexity of O(n), where n is the number of elements in the array, and should not use any additional space that scales with the input size.
"""

def find_max_element(nums):
    if not nums:
        return None
    
    max_element = nums[0]
    for num in nums[1:]:
        if num > max_element:
            max_element = num
    return max_element