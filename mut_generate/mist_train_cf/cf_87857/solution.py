"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of integers as input and returns the sorted list in reverse order. The function should not use any built-in sorting functions or libraries. Optimize the function for efficiency in terms of time and space complexity, and handle edge cases such as an empty list, a list with only one element, or a list with duplicate elements.
"""

def bubble_sort(nums):
    # If the list is empty or has only one element, return the list
    if len(nums) <= 1:
        return nums
    
    # Bubble sort algorithm
    n = len(nums)
    for i in range(n):
        # Flag to check if any swaps were made in the current pass
        swapped = False
        for j in range(n-1-i):
            # Swap adjacent elements if they are in the wrong order
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        # If no swaps were made in the current pass, the list is already sorted
        if not swapped:
            break
    
    # Return the sorted list in reverse order
    return nums[::-1]