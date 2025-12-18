"""
QUESTION:
Construct a function called bubble_sort to sort an array of integers in ascending order using the Bubble Sort algorithm. The function should take a list of integers as input and return the sorted list. The function should have a time complexity of O(n²) in the worst-case and average scenarios, and a space complexity of O(1).
"""

def bubble_sort(nums):
    """
    Sorts an array of integers in ascending order using the Bubble Sort algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list of integers.
    """
    n = len(nums)
    
    for i in range(n):
        swapped = False
        
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        for j in range(0, n-i-1):
            # Compare the adjacent elements and swap if they are in wrong order
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True

        # If no two elements were swapped by inner loop, the array is sorted
        if not swapped:
            break

    return nums