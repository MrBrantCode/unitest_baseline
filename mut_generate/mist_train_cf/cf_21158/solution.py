"""
QUESTION:
Given an array of positive integers, find the longest subarray with a total sum equal to the given sum. The subarray must contain at least one odd integer and one even integer. If there are multiple subarrays with the same length, return the subarray with the smallest starting index. Implement a function named `find_subarray(arr, target_sum)` that takes the array and the target sum as input and returns the longest valid subarray.
"""

def find_subarray(arr, target_sum):
    left = 0
    right = 0
    subarray = []
    oddCount = 0
    evenCount = 0
    longestSubarray = []

    while right < len(arr):
        subarray.append(arr[right])
        if arr[right] % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

        while sum(subarray) > target_sum:
            if arr[left] % 2 == 0:
                evenCount -= 1
            else:
                oddCount -= 1
            subarray = subarray[1:]
            left += 1

        if sum(subarray) == target_sum and oddCount > 0 and evenCount > 0:
            if len(subarray) > len(longestSubarray):
                longestSubarray = subarray[:]

        right += 1

    return longestSubarray