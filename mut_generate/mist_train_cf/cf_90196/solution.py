"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of integers as input and returns the list with all duplicates removed. The function should not use any additional data structures and should preserve the original order of elements. The time complexity should be O(n^2) and space complexity should be O(1).
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