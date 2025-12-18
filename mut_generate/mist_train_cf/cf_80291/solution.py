"""
QUESTION:
Given a circular integer array `nums`, return the next smaller number for every element in `nums`. The next smaller number of a number `x` is the first smaller number to its traversing-order next in the array. If it doesn't exist, return `-1` for this number. The function name is `nextSmallerElements(nums)` and it should take an array `nums` as input and return an array of integers as output. The length of the input array `nums` is between 1 and 10^4 and the range of each number in `nums` is between -10^9 and 10^9.
"""

def nextSmallerElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n * 2):
        while stack and (nums[stack[-1]] > nums[i % n]):
            res[stack.pop()] = nums[i % n]
        stack.append(i % n)

    return res