"""
QUESTION:
Implement the `find_ranges(nums, start, end)` function, which takes a sorted list of integers `nums`, and two integer parameters `start` and `end`. The function should return a list of strings representing ranges of numbers from `start` to `end` that are missing from `nums`. Single missing numbers should be represented as a single string, while multiple consecutive missing numbers should be represented as a range string. If `start` and `end` are not in `nums`, they should also be included in the output if they are part of the missing ranges.
"""

def find_ranges(nums, start, end):
    result = []
    if start < nums[0]:
        if start + 1 == nums[0]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[0]-1}")
    for i in range(len(nums) - 1):
        if nums[i] + 1 < nums[i + 1]:
            if nums[i] + 2 == nums[i + 1]:
                result.append(str(nums[i] + 1))
            else:
                result.append(f"{nums[i]+1}->{nums[i+1]-1}")
    if nums[-1] < end:
        if nums[-1] + 1 == end:
            result.append(str(end))
        else:
            result.append(f"{nums[-1]+1}->{end}")
    return result