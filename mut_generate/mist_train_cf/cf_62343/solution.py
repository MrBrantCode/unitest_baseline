"""
QUESTION:
Write a function `frequencySort(nums)` that takes an array of integers `nums` and returns the sorted array in decreasing order based on the frequency of the values. If multiple values have the same frequency, sort them in increasing order. The input array `nums` has a length between 1 and 100, and each element in the array is between -100 and 100.
"""

def frequencySort(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    nums.sort(key=lambda x: (-freq[x], x))
    return nums