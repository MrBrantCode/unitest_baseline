"""
QUESTION:
Implement a function named bubble_sort that takes a list of integers as input and sorts the list in ascending order using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) in the average and worst-case scenarios, and O(n) in the best-case scenario. The space complexity of the function should be O(1).
"""

def bubble_sort(nums):
    n = len(nums)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break

    return nums