"""
QUESTION:
Create a function called `bubble_sort` that takes an array of integers as input and returns a sorted array from smallest to largest using the bubble sort algorithm. The input array can contain any number of integers and may or may not be sorted initially. The function should not use any built-in sorting functions and should only utilize the bubble sort method.
"""

def bubble_sort(nums):
    """
    This function sorts an array of integers using the bubble sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A sorted list of integers from smallest to largest.
    """
    n = len(nums)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        already_sorted = True
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                # Swap values
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                # Since we had to swap two elements,
                # we need to iterate over the list again.
                already_sorted = False
        # If there were no swaps during the last iteration,
        # the list is already sorted, and we can terminate
        if already_sorted:
            break
    return nums