"""
QUESTION:
Given an array containing N integers and a positive integer K, find the length of the longest sub array with sum of the elements divisible by the given value K.
Example 1:
Input:
A[] = {2, 7, 6, 1, 4, 5}
K = 3
Output: 4
Explanation:The subarray is {7, 6, 1, 4}
with sum 18, which is divisible by 3.
Example 2:
Input:
A[] = {-2, 2, -5, 12, -11, -1, 7}
K = 3
Output: 5
Explanation:
The subarray is {2,-5,12,-11,-1} with
sum -3, which is divisible by 3.
 
Your Task:
The input is already taken care of by the driver code. You only need to complete the function longSubarrWthSumDivByK() that takes an array (arr), sizeOfArray (n), positive integer K, and return the length of the longest subarray which has sum divisible by K. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1<=N,K<=10^{6}
-10^{5}<=A[i]<=10^{5}
"""

def longest_subarray_with_sum_divisible_by_k(arr, K):
    n = len(arr)
    t = 0
    m = 0
    d = {}
    
    for i in range(n):
        t += arr[i]
        if t % K == 0:
            m = max(m, i + 1)
        if t % K in d:
            m = max(m, i - d[t % K])
        else:
            d[t % K] = i
    
    return m