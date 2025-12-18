"""
QUESTION:
Write a function named `remove_duplicates` that takes an array of integers as input and returns the array with all duplicates removed and sorted in ascending order. The function should not use any additional data structures such as sets or dictionaries.
"""

def remove_duplicates(nums):
    """
    Removes duplicates from a list of integers and returns the list in ascending order.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: The list of integers with duplicates removed, in ascending order.
    """
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