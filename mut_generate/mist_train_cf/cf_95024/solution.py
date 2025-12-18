"""
QUESTION:
Implement a function called `bubble_sort(nums)` that sorts a list of integers in increasing order without using any built-in sorting functions or libraries. The function should handle edge cases such as an empty list, a list with only one element, or a list with duplicate elements, and optimize for efficiency in terms of time and space complexity.
"""

def bubble_sort(nums):
    # Check for edge cases
    if len(nums) <= 1:
        return nums

    # Start with the entire list
    n = len(nums)
    # Iterate through the list n-1 times
    for i in range(n - 1):
        # Flag to check if any swap occurred during the iteration
        swapped = False
        # Iterate through the list from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # If no swap occurred during the iteration, the list is already sorted
        if not swapped:
            break

    return nums