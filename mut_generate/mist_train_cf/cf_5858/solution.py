"""
QUESTION:
Implement a function `comb_sort` that sorts a list of numbers in ascending order using the comb sort algorithm, without using any built-in sorting functions or methods. The input is a list of integers, and the output should be the sorted list. The function should not use any external libraries or built-in sorting functions.
"""

def comb_sort(nums):
    """
    Sorts a list of numbers in ascending order using the comb sort algorithm.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The sorted list of integers.
    """
    gap = len(nums)
    shrink = 1.3
    sorted_flag = False

    while not sorted_flag:
        gap = int(gap / shrink)
        
        if gap < 1:
            gap = 1
            sorted_flag = True
        
        i = 0
        while i + gap < len(nums):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                sorted_flag = False
            i += 1

    return nums