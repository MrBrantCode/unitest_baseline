"""
QUESTION:
Given a list of integers, create a function `remove_duplicates(nums)` that returns the list with only unique elements, in sorted order. The function must have a time complexity of O(n) and a space complexity of O(1), without using any additional data structures. The function should modify the original list to remove duplicate elements.
"""

def remove_duplicates(nums):
    # Sort the list to group duplicate elements together
    nums.sort()

    # Initialize two pointers: one for the current element, and one for the next unique element
    current = 0
    next_unique = 1

    while next_unique < len(nums):
        # If the next element is unique, move it to the current position
        if nums[current] != nums[next_unique]:
            current += 1
            nums[current] = nums[next_unique]

        next_unique += 1

    # Truncate the list to the unique elements
    del nums[current+1:]

    return nums