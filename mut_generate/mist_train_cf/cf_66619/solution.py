"""
QUESTION:
You are to create a function called `summaryRanges(nums)` which takes a sorted unique integer array `nums` and returns the smallest sorted list of ranges that encapsulates all the integers in the array. The ranges should be represented as follows: if `a` is not equal to `b`, it should be displayed as `"a->b"`, and if `a` is equal to `b`, it should be displayed as `"a"`. The length of `nums` is between 0 and 1000, the values of `nums[i]` range from `-231` to `231 - 1`, all values in `nums` are unique, and `nums` is sorted in ascending order.
"""

def summaryRanges(nums):
    if not nums:
        return []
    ranges = []
    start = end = nums[0]
    for num in nums[1:]:
        if num - end > 1:   
            ranges.append(f"{start}->{end}" if start != end else f"{start}")
            start = end = num  
        else:
            end = num   
    ranges.append(f"{start}->{end}" if start != end else f"{start}")
    return ranges