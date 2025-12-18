"""
QUESTION:
Write a function named `longestIncreasingSubsequence` that takes a list of integers as input and returns the length of the longest increasing subsequence within the list. The subsequence should be a contiguous or non-contiguous sequence of numbers where each number is greater than the previous one. For example, in the array [2, 3, 5, 4, 7, 9, 6, 8], the longest increasing subsequence is [2, 3, 4, 6, 8] or [2, 3, 4, 7, 9], and the function should return 5.
"""

def longestIncreasingSubsequence(arr): 
    n = len(arr) 
   
    # Initialize lengths array as 1 for all elements
    lis = [1]*n 
  
    # Compute optimized LIS values 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    # Return maximum length
    return max(lis)