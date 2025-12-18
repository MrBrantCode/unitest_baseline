"""
QUESTION:
Remove duplicates from a given array of integers in-place in non-decreasing order. Implement a function `remove_duplicates(nums)` that takes an array of integers as input and returns the array with duplicates removed, maintaining the order of the remaining elements. The solution should have O(n log n) time complexity due to sorting and O(1) space complexity without using any additional data structures or allocating extra space.
"""

def remove_duplicates(nums):
    # Sort the array in non-decreasing order
    nums.sort()
    
    # Initialize two pointers, one for the current element and one for the next unique element
    current = 0
    unique = 0
    
    # Iterate through the array
    while current < len(nums):
        # If the current element is different from the next unique element, update the next unique element
        if nums[current] != nums[unique]:
            unique += 1
            # Swap the current element with the next unique element
            nums[unique], nums[current] = nums[current], nums[unique]
        current += 1
    
    # Return the new array without duplicates
    return nums[:unique+1]