"""
QUESTION:
Implement a function called `bubble_sort` that takes an array of integers as input and returns the array sorted in ascending order. The function must implement the Bubble Sort algorithm and cannot use any built-in sorting functions or algorithms.
"""

def bubble_sort(nums):
    """
    Sorts the input array of integers in ascending order using the Bubble Sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers in ascending order.
    """
    n = len(nums)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap them if they are in the wrong order
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        # If there were no swaps during the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break
    return nums