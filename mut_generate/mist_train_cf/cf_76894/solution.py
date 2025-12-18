"""
QUESTION:
Write a function `summaryRanges(nums)` that takes a sorted, unique integer array `nums` and returns the smallest sorted list of ranges that encapsulates all the integers in the array. Each integer in `nums` must be covered by a single range. The range `[a,b]` should be represented as `"a->b"` if `a` is not equal to `b`, and `"a"` if `a` is equal to `b`. The length of `nums` is between 0 and 20, the values of `nums[i]` range from `-2^31` to `2^31 - 1`, and all values in `nums` are unique and sorted in ascending order.
"""

def summaryRanges(nums):
    if not nums:
        return []
    res = []
    start = nums[0]
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1] + 1:
            if start != nums[i-1]:
                res.append(str(start) + '->' + str(nums[i-1]))
            else:
                res.append(str(start))
            start = nums[i]
    if start != nums[-1]:
        res.append(str(start) + '->' + str(nums[-1]))
    else:
        res.append(str(start))
    return res