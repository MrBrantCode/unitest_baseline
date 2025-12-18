"""
QUESTION:
Create a function named `remove_duplicates` that takes a list `nums` as input and returns the list with only the unique elements, while maintaining a time complexity of O(n) and a space complexity of O(1). The input list can be modified in-place.
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