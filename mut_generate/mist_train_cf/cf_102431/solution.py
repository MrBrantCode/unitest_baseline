"""
QUESTION:
Write a Python function called `rearrange_array` that takes an array of integers and a target sum as input and returns the rearranged array such that the sum of adjacent elements is always less than or equal to the target sum. The function should rearrange the array in-place and return the modified array. The time complexity of the solution should be O(n log n) due to sorting, where n is the number of elements in the array.
"""

def rearrange_array(nums, target):
    """
    This function rearranges the input array such that the sum of adjacent elements 
    is always less than or equal to the target sum.

    Args:
    nums (list): A list of integers.
    target (int): The target sum.

    Returns:
    list: The rearranged array.
    """
    nums.sort()  # Sort the array in ascending order
    result = []  # Initialize an empty list to store the result
    i, j = 0, len(nums) - 1  # Initialize two pointers, one at the start and one at the end of the array

    while i <= j:  # Continue the loop until the two pointers meet
        if len(result) == 0 or result[-1] + nums[i] <= target:  # If the sum of the last element in the result and the current smallest number is less than or equal to the target
            result.append(nums[i])  # Add the current smallest number to the result
            i += 1  # Move the left pointer to the right
        else:
            result.append(nums[j])  # If not, add the current largest number to the result
            j -= 1  # Move the right pointer to the left

    return result  # Return the rearranged array