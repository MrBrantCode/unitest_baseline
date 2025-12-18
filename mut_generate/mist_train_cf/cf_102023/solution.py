"""
QUESTION:
Given a list of numbers and an integer k, find the longest increasing subsequence of length greater than or equal to k. An increasing subsequence is a sequence of numbers in which each number is greater than the previous number. The subsequence does not have to be contiguous.

Write a function named longest_increasing_subsequence that takes in a list of numbers and an integer k, and returns the longest increasing subsequence of length greater than or equal to k. If there are multiple subsequences with the same length, return any one of them.

The function should have the following signature:
def longest_increasing_subsequence(arr: List[int], k: int) -> List[int]:

Restrictions: 
- The input list contains only positive integers. 
- Time Complexity: O(n^2)
- Space Complexity: O(n)
"""

def longest_increasing_subsequence(arr, k):
    n = len(arr)
    lis = [[num] for num in arr]
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and len(lis[i]) < len(lis[j]) + 1:
                lis[i] = lis[j] + [arr[i]]
    
    longest_subsequence = max(lis, key=len)
    
    return longest_subsequence if len(longest_subsequence) >= k else []