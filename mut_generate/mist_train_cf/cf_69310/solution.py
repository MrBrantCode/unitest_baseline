"""
QUESTION:
Given an array of integers `nums`, write a function `findLongest(nums)` to compute the total count of the longest strictly ascending subsequences present within this sequence. The length of `nums` is within the range `1 <= nums.length <= 2000` and the elements of `nums` are within the range `-10^6 <= nums[i] <= 10^6`.
"""

def findLongest(nums):
    n = len(nums)
    lengths = [1]*n
    counts = [1]*n
    max_len, max_count = 0, 0

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j]+1 > lengths[i]:
                    lengths[i] = lengths[j]+1
                    counts[i] = counts[j]
                elif lengths[j]+1 == lengths[i]:
                    counts[i] += counts[j]
                    
        if lengths[i] > max_len:
            max_len = lengths[i]
            max_count = counts[i]
        elif lengths[i] == max_len:
            max_count += counts[i]

    return max_count