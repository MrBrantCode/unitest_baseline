"""
QUESTION:
Write a Python function `longestSubarray` that takes three lists of integers and returns the maximum sum of the longest contiguous subarray present in all three lists. The function should use backtracking and dynamic programming, and it should handle cases where the lists contain negative numbers. The function should have a time complexity of O(N^3) and a space complexity of O(N^3), where N is the average length of the lists.
"""

def longestSubarray(arr1, arr2, arr3, m, n, o, sum1=0, sum2=0, sum3=0, memo=None):
    if memo is None:
        memo = {}
    if m == 0 or n == 0 or o == 0:
        return 0

    # if the result is already computed
    if (m, n, o, sum1, sum2, sum3) in memo:
        return memo[(m, n, o, sum1, sum2, sum3)]

    else: 
        # check if all array elements are same
        if arr1[m - 1] == arr2[n - 1] == arr3[o - 1]:
            sum1 += arr1[m - 1]
            sum2 += arr2[n - 1]
            sum3 += arr3[o - 1]

            memo[(m, n, o, sum1, sum2, sum3)] = max(1 + longestSubarray(arr1, arr2, arr3, m - 1, n - 1, o - 1, sum1, sum2, sum3, memo), \
            sum1, sum2, sum3)

        else:
            memo[(m, n, o, sum1, sum2, sum3)] = max(longestSubarray(arr1, arr2, arr3, m - 1, n, o, sum1, sum2, sum3, memo), \
            longestSubarray(arr1, arr2, arr3, m, n - 1, o, sum1, sum2, sum3, memo), \
            longestSubarray(arr1, arr2, arr3, m, n, o - 1, sum1, sum2, sum3, memo), \
            sum1, sum2, sum3)
    
    return memo[(m, n, o, sum1, sum2, sum3)]

def longestCommonSumSubarray(arr1, arr2, arr3):
    return longestSubarray(arr1, arr2, arr3, len(arr1), len(arr2), len(arr3))