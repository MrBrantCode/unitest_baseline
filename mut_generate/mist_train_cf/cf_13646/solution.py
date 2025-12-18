"""
QUESTION:
Implement a function called `bubble_sort` that sorts a list of elements in ascending order, using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the list. The function should sort the list in-place, without using any additional data structures.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums