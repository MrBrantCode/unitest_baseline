"""
QUESTION:
Write a function `findShortestSubArray(nums)` that finds the smallest possible length of a contiguous subarray of `nums` that has the same degree as `nums`, and also returns the sum of all the elements in the subarray. The degree of an array is defined as the maximum frequency of any one of its elements. The function should return a tuple containing the length of the shortest subarray and the sum of its elements. The input array `nums` will have a length between 1 and 50,000, and will contain integers between 0 and 49,999.
"""

def findShortestSubArray(nums):
    left, right, count = {}, {}, {}
    for i, x in enumerate(nums):
        if x not in left: left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    max_freq = max(count.values())
    min_length, min_sum = float('inf'), 0

    for x in count:
        if count[x] == max_freq:
            if right[x] - left[x] + 1 < min_length: 
                min_length = right[x] - left[x] + 1
                min_sum = sum(nums[left[x]: right[x]+1])

    return (min_length, min_sum)