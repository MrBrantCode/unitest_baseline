"""
QUESTION:
Write a function `find_first_and_last_index` to find the first and last index of a target element in a sorted array. The array contains integers in ascending order and may have duplicate values. The function should return the first and last index of the target element if it exists in the array; otherwise, return None or a message indicating the element is not found.
"""

def find_first_and_last_index(nums, target):
    """
    Find the first and last index of a target element in a sorted array.

    Args:
    nums (list): A sorted list of integers in ascending order.
    target (int): The target element to find.

    Returns:
    tuple or None: A tuple containing the first and last index of the target element if found, otherwise None.
    """
    def binary_search(nums, target, find_first):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first_index = binary_search(nums, target, True)
    if first_index == -1:
        return None
    last_index = binary_search(nums, target, False)
    return (first_index, last_index)