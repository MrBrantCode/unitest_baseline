"""
QUESTION:
Write a function `maximumGap(nums)` that takes an array of integers `nums` as input and returns the largest gap between two consecutive elements when the array is sorted in ascending order. If the array has less than two elements, the function should return `0`. The length of `nums` should be between 1 and 10^4, inclusive, and each element in `nums` should be between 0 and 10^9, inclusive. The function should operate in linear time and space complexity.
"""

def maximumGap(nums):
    if len(nums) < 2 or min(nums) == max(nums):
        return 0
    min_, max_ = min(nums), max(nums)
    size = (max_-min_)/(len(nums)-1)
    bucket = [[None, None] for _ in range(int((max_-min_)//size+1))]
    for n in nums:
        b = bucket[int((n-min_)//size)]
        b[0] = n if b[0] is None else min(b[0], n)
        b[1] = n if b[1] is None else max(b[1], n)
    bucket = [b for b in bucket if b[0] is not None]
    return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))