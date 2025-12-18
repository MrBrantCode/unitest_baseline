"""
QUESTION:
Given an integer n and array of integers, returns the Longest Increasing subsequence which is lexicographically smallest corresponding to the indices of the elements.
LIS  of a given sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}. 
 
Note - A subsequence S1 is lexicographically smaller than a subsequence S2 if in the first position where a and b differ, subsequence a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example , {1, 2, 3, 6, 7} is lexographically smaller than {1, 2, 3, 8, 10} and {1, 2, 3} is lexographically smaller than {1, 2, 3, 1}.
 
Example 1:
Input:
n = 16
arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
Output:
0 4 6 9 13 15 
Explanation:
longest Increasing subsequence is 0 4 6 9 13 15  and the length of the longest increasing subsequence is 6.
Example 2:
Input:
n = 1
arr = [1]
Output:
1
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestIncreasingSubsequence() which takes integer n and array arr and returns the longest increasing subsequence.
Expected Time Complexity: O(n^{2})
Expected Space Complexity: O(n)
Constraint:
1 <= n < = 1000
1 <= arr[i] <= 50000
"""

def longest_increasing_subsequence(n, arr):
    # Initialize result, dp array, and path array
    res, dp, path = [], [1] * n, [i for i in range(n)]
    lisInd = lis = 0
    
    # Dynamic programming to find the longest increasing subsequence
    for i in range(n):
        for prev in range(i):
            if arr[prev] < arr[i] and dp[prev] + 1 > dp[i]:
                dp[i] = dp[prev] + 1
                path[i] = prev
                if dp[i] > lis:
                    lis = dp[i]
                    lisInd = i
    
    # Reconstruct the longest increasing subsequence
    while path[lisInd] != lisInd:
        res.append(arr[lisInd])
        lisInd = path[lisInd]
    res.append(arr[lisInd])
    
    # Return the result in the correct order
    return res[::-1]