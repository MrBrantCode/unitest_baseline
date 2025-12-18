"""
QUESTION:
Implement the `reverseList` function, which takes a list as input and reverses its order without using the built-in `reverse()` function or any other list methods. The function should only use indexing and basic operations to reverse the list.
"""

def reverseList(nums):
    start = 0
    end = len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums