"""
QUESTION:
Given an array A[] with N elements , you need to find the sum all sub arrays of array A. Since the sum could be very large print the sum modulo (10^{9}+7).
Example 1:
Input:
N = 3
A[] = {1, 2, 3}
Output: 20
Explanation:
All subarrays are [1], [2], [3],
[1,2], [2,3], [1,2,3].
Thus total sum is 20.
 
Example 2:
Input:
N = 2
A[] = {1, 3}
Output: 8
Your Task:  
You don't need to read input or print anything. Your task is to complete the function subarraySum() which takes the array A[] and its size N as inputs and returns the sum.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints :
1 ≤ N ≤ 10^{5}
1 ≤ A[] ≤ 10^{9}
"""

def calculate_subarray_sum(A, N):
    MOD = 1000000007
    total_sum = 0
    for i in range(N):
        total_sum += A[i] * (i + 1) * (N - i)
    return total_sum % MOD