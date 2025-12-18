"""
QUESTION:
Implement a function `find_duplicate_indices(nums)` that takes an array of integers `nums` as input, where the integers range from -1000 to 1000 and the array length is between 1 and 1000. The function should return the indices of the first occurrence of each duplicate element in the input array, handling duplicate elements and achieving a time complexity of O(n) and a space complexity of O(1).
"""

def find_duplicate_indices(nums):
    duplicates = set()
    indices = []
    
    for i, num in enumerate(nums):
        if num in duplicates:
            indices.append(nums.index(num))
        else:
            duplicates.add(num)
    
    return indices