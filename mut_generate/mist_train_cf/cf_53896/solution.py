"""
QUESTION:
Given a non-negative integer in the range [0, 10^8], write a function named `maximumSwap` to swap two digits at most once to get the maximum valued number. Return the maximum valued number as an integer and the indices of the swapped digits as a tuple. If no swap is made, return the original number and (-1, -1) for the indices. The indices are 0-indexed.
"""

def maximumSwap(num):
    nums = list(str(num))
    last = {int(v): i for i, v in enumerate(nums)}

    for i in range(len(nums)):
        for d in range(9, int(nums[i]), -1):
            if last.get(d) and last[d] > i:
                nums[i], nums[last[d]] = nums[last[d]], nums[i]
                return int(''.join(nums)), (i, last[d])
    return num, (-1, -1)