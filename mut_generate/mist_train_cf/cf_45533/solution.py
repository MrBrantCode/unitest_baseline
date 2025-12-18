"""
QUESTION:
Write a function named `bubble_sort` that takes a list of integers as input and returns the sorted list using the bubble sort algorithm. The function should repeatedly iterate through the list, comparing adjacent elements and swapping them if they are in the wrong order, until the list is sorted. The input list can contain duplicate elements and is not guaranteed to be sorted. The function should return the sorted list.
"""

def bubble_sort(nums):
    """
    Sorts a list of integers using the bubble sort algorithm.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The sorted list of integers.
    """
    # Create a copy of the input list to avoid modifying the original list
    nums_copy = nums.copy()

    n = len(nums_copy)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n-i-1):
            # If we come across an element that is greater than the next element
            if nums_copy[j] > nums_copy[j+1]:
                # Swap them
                nums_copy[j], nums_copy[j+1] = nums_copy[j+1], nums_copy[j]
                # Set the flag to True so we'll loop again after this iteration
                swapped = True
        # If there were no swaps during the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break
    return nums_copy