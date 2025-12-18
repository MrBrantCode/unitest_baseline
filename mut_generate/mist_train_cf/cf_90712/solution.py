"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of integers as input and returns a new list containing the unique elements from the original list. The function should have a time complexity of O(n log n) or better.
"""

def remove_duplicates(nums):
    """
    This function removes duplicates from a list of integers.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A new list containing the unique elements from the original list.

    Time complexity: O(n log n) due to sorting operation.
    """

    # Sort the list
    nums.sort()

    # Create a new list to store the unique elements
    unique_list = []

    # Iterate through the sorted list
    for i in range(len(nums)):
        # If the current element is not equal to the next element, add it to the unique list
        if i == len(nums) - 1 or nums[i] != nums[i + 1]:
            unique_list.append(nums[i])

    # Return the unique list
    return unique_list