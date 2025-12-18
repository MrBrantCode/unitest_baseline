"""
QUESTION:
Implement a function called `bubbleSort` that sorts a list of numbers using the Bubble Sort algorithm. The function should take a list of numbers as input and return the sorted list. The function should optimize the sorting process by stopping early if no swaps are made in a pass, and it should use a temporary variable to store the swapped elements. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def bubbleSort(nums):
    n = len(nums)
    while True:
        swapped = False
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
        n -= 1
    return nums