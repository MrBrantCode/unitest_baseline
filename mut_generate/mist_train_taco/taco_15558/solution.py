"""
QUESTION:
Given an array arr[] of N integers. A subsequence of arr[] is called Bitonic if it is first increasing then decreasing. Print the max sum bitonic subsequence.
Example 1:
Input :
N = 9
arr[] = {1, 15, 51, 45, 33,
                   100, 12, 18, 9}
Output : 194
Explanation :
Bi-tonic Sub-sequence are :
{1, 51, 9} or {1, 51, 100, 18, 9} or
{1, 15, 51, 100, 18, 9}  or
{1, 15, 45, 100, 12, 9}  or
{1, 15, 45, 100, 18, 9} .. so on           
Maximum sum Bi-tonic sub-sequence is 1 +
15 + 51 + 100 + 18 + 9 = 194
Example 2:
Input :
N = 6
arr[] = {80, 60, 30, 40, 20, 10}
Output :
210
Explanation :
Here the sequence is strinctly decreasing.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function leftIndex() which takes the array arr[] and its size N as inputs and returns the maximum Bitonic sequence sum.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1<=N<=10^{3}
1<=arr[]<=10^{5}
"""

def max_sum_bitonic_subsequence(arr, N):
    dp1 = [arr[i] for i in range(N)]
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j] and dp1[i] < dp1[j] + arr[i]:
                dp1[i] = arr[i] + dp1[j]
    
    dp2 = [arr[i] for i in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, -1):
            if arr[i] > arr[j] and dp2[i] < dp2[j] + arr[i]:
                dp2[i] = arr[i] + dp2[j]
    
    maxi = float('-inf')
    for i in range(N):
        maxi = max(maxi, dp1[i] + dp2[i] - arr[i])
    
    return maxi