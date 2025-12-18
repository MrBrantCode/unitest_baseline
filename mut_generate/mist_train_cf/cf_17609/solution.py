"""
QUESTION:
Implement the `bubble_sort` function to sort a list of numbers in increasing order without using any built-in sorting functions or libraries. The function should have a time complexity of O(n^2) and a space complexity of O(1). The solution should be stable, meaning that elements with equal values should retain their relative order after sorting.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        # Flag to check if any swaps were made in the current pass
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                # Swap the elements
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        # If no swaps were made in the current pass, the list is already sorted
        if not swapped:
            break
    return nums