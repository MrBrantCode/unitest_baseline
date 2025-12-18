"""
QUESTION:
Find the maximum sum of a contiguous subarray of size 'k' in a given array with the following restrictions: the subarray cannot contain any duplicate elements, must have an even number of elements, and must have elements in strictly increasing order. If multiple subarrays have the same maximum sum, return the subarray with the smallest starting index and the smallest ending index. Implement the function `find_max_sum_subarray(arr, k)` to solve this problem.
"""

def find_max_sum_subarray(arr, k):
    start = 0
    maxSum = 0
    result = []

    for i in range(len(arr)-k+1):
        if i > start and arr[i] <= arr[i-1]:
            start = i
        subarray = arr[i:i+k]
        subarraySum = sum(subarray)
        if subarraySum > maxSum and len(set(subarray)) == k and k % 2 == 0:
            maxSum = subarraySum
            result = subarray

    return result