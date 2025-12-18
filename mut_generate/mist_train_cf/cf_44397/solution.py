"""
QUESTION:
Design a function named `bubble_sort` that sorts a given list of numerical values in ascending order, ensuring that each number is placed in a position such that it is greater than or equal to the preceding number and less than or equal to the following number. The function should not use any built-in sorting functions and should have a time complexity of O(n^2) or less.
"""

def bubble_sort(nums):
    """
    Sorts a given list of numerical values in ascending order using the bubble sort algorithm.

    Args:
        nums (list): A list of numerical values.

    Returns:
        list: A sorted list in ascending order.
    """
    n = len(nums)
    
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        
        # Start looking at each item of the list one by one, comparing it with its adjacent value
        for j in range(n - i - 1):
            # With every comparison, we are checking if the current element is greater than its adjacent element
            if nums[j] > nums[j + 1]:
                # If we come across an element that is greater than its adjacent element, swap them
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                # Set the flag to True so we'll loop again after this iteration
                swapped = True
        
        # If there were no swaps during the last iteration, the list is already sorted, and we can terminate
        if not swapped:
            break
    
    return nums