"""
QUESTION:
Write a function `remove_duplicates(nums)` that takes a list of integers as input, removes duplicates without using any additional data structures, and maintains the original order of elements. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def remove_duplicates(nums):
    # Iterate over each element in the list
    for i in range(len(nums)):
        # Check if the current element has already been encountered
        j = i + 1
        while j < len(nums):
            # If duplicate found, remove it
            if nums[j] == nums[i]:
                nums.pop(j)
            else:
                j += 1
    
    return nums