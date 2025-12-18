"""
QUESTION:
Implement a function named `remove_duplicates(nums)` that takes an array of integers as input. The function should sort the array in ascending order, remove any duplicate values, and return the modified array. The function must not use any additional data structures such as sets or dictionaries. The array can contain negative numbers.
"""

def remove_duplicates(nums):
    # Sort the array
    nums.sort()

    # Initialize the pointer to the current unique value
    i = 0

    # Iterate through the array
    for j in range(1, len(nums)):
        # If the current value is not equal to the value at index `i`,
        # we have encountered a new unique value
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # Return the modified array from index 0 to `i`
    return nums[:i+1]