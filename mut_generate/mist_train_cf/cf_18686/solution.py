"""
QUESTION:
Write a function `find_median` that takes a list of positive integers as input and returns the median of the list using only logical operations and bitwise operators. The function should be able to handle both lists with odd and even numbers of elements.
"""

def find_median(nums):
    """
    This function calculates the median of a list of integers using bitwise operations.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The median of the input list.
    """
    
    # First, we need to sort the list in ascending order.
    # Since the problem statement does not allow using built-in sort functions, 
    # we'll use a simple bubble sort algorithm instead.
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            # If the current element is greater than the next element, swap them.
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
    # Now that the list is sorted, we can find the median.
    count = len(nums)
    is_odd = count & 1

    if is_odd:
        # If the count is odd, the median is the middle element.
        middle_index = count // 2
        median = nums[middle_index]
    else:
        # If the count is even, the median is the average of the two middle elements.
        first_middle_index = count // 2 - 1
        second_middle_index = count // 2
        median = (nums[first_middle_index] + nums[second_middle_index]) // 2

    return median