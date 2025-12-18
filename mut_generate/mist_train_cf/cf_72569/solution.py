"""
QUESTION:
Given an integer array `arr`, remove a subarray (can be empty) from `arr` such that the remaining elements in `arr` are non-decreasing and the sum of the remaining elements is maximum. Return the length of the shortest subarray to remove. 

The input array `arr` has the following constraints: `1 <= arr.length <= 10^5` and `0 <= arr[i] <= 10^9`. The function to implement is `findLengthOfShortestSubarray(arr)`.
"""

def findLengthOfShortestSubarray(arr):
    n = len(arr)
    begin, end = 0, n - 1
    while begin < n - 1 and arr[begin] <= arr[begin + 1]:
        begin += 1
    if begin == n - 1:
        return 0
    while end > begin and arr[end] >= arr[end - 1]:
        end -= 1
    ans = min(n - begin - 1, end)
    i = 0
    j = end
    while i <= begin and j < n:
        if arr[i] <= arr[j]:
            ans = min(ans, j - i - 1)
            i += 1
        else:
            j += 1
    return ans