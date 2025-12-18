"""
QUESTION:
Design a function `remove_all_duplicates` that takes an array of integers as input and returns the array with all duplicates removed while maintaining the original order of the remaining elements. The function should have a time complexity of O(n) and use only a constant amount of additional space, where n is the size of the input array. The function should be able to handle arrays of size up to 10^7 elements.
"""

def remove_all_duplicates(nums):
    seen = set()
    result = []
    
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result