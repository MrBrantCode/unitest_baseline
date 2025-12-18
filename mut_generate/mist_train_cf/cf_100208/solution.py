"""
QUESTION:
Create a function named `find_duplicate` that finds the first duplicate number in a given list of integers without using any additional memory. The function should take a list of integers as input and return the first duplicate number found, or -1 if no duplicates are found.
"""

def find_duplicate(nums):
    """
    Given a list of integers, finds the first duplicate number within the list.

    Args:
    - nums: a list of integers

    Returns:
    - the first duplicate number found within the list
    - -1 if no duplicates are found

    Time Complexity:
    - O(nlogn), where n is the number of integers in the list

    Space Complexity:
    - O(1)
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]
    return -1