"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of numbers as input and returns the numbers in ascending order. The function should not use any built-in sorting functions or methods and should have a time complexity of O(n^2), where n is the number of elements in the list.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        # Set a flag to check if any swap occurs in this pass
        swapped = False
        for j in range(0, n-i-1):
            # Swap if the current number is greater than the next number
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        # If no swap occurs in this pass, the list is already sorted
        if not swapped:
            break
    return nums