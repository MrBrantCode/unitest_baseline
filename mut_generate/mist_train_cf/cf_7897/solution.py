"""
QUESTION:
Write a function `removeElement` that takes an integer array `arr` and an integer `val` as input, removes all elements with the value `val` from the array in-place, and returns the new length of the array. The function should not use any additional data structures or modify the size of the original array, and it should have a time complexity of O(n), where n is the length of the array. The function should set the removed elements to zero to indicate their removal, as the array size cannot be modified.
"""

def removeElement(nums, val):
    """
    Removes all elements with the value `val` from the array `nums` in-place and returns the new length of the array.

    Args:
    nums (list): The input array.
    val (int): The value to be removed.

    Returns:
    int: The new length of the array.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    for i in range(count, len(nums)):
        nums[i] = 0
    return count