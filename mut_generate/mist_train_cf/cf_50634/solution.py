"""
QUESTION:
Write a function `kth_largest_sum` that takes an array of integers and an integer `k` as input and returns the kth highest sum of all possible subarrays. If `k` is larger than the total number of subarrays, return an error message. Optimize the solution for optimal time complexity, handling negative numbers and zeros effectively.
"""

from heapq import nlargest
from itertools import combinations

def kth_largest_sum(arr, k):
    # get the length of the list
    n = len(arr)
    
    # total possible subarrays is n*(n+1)/2, if k is greater than this return error
    if k > n*(n+1)//2:
        return 'Error: k is greater than the total number of subarrays.'

    # list to store all the subarray sums.
    subarray_sums = []

    # iterate through the list for all possible subarrays and compute the sum using nested loop
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            subarray_sums.append(total)

    # return the k-th largest sum
    return nlargest(k, subarray_sums)[-1]