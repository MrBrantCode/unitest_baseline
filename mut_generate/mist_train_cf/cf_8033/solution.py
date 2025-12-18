"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of integers as input and sorts the list in ascending order using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1). The function must not use any built-in sorting functions or libraries.
"""

def bubble_sort(nums):
    """
    Sorts a list of integers in ascending order using the Bubble Sort algorithm.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
    nums (list): A list of integers to be sorted.

    Returns:
    list: The sorted list of integers.
    """
    n = len(nums)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums