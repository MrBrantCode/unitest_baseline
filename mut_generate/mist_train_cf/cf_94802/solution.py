"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of numbers as input, sorts them in increasing order without using any built-in sorting functions or libraries, and returns the sorted list. The solution should have a time complexity of O(n^2), where n is the length of the list, and a space complexity of O(1). The sorting algorithm should be stable, meaning that elements with equal values should retain their relative order after sorting.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums