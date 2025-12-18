"""
QUESTION:
Create a function `find_nth_smallest_number` that takes an integer `n` and an unsorted list of numbers as input and returns the nth smallest number in the list. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def find_nth_smallest_number(n, nums):
    nums.sort()  # O(n log n)
    return nums[n-1]