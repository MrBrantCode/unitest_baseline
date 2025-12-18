"""
QUESTION:
Write a function `find_middle(nums)` that takes a list of integers `nums` as input and returns the middle element(s) of the list. If the length of the list is odd, return the single middle element. If the length of the list is even, return the two middle elements.
"""

def find_middle(nums):
    n = len(nums)
    mid = n//2
    if n%2 == 0:   # if number of elements in the list is even
        return nums[mid-1:mid+1]
    else:          # if number of elements in the list is odd
        return [nums[mid]]