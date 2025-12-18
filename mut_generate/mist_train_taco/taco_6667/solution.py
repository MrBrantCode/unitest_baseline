"""
QUESTION:
Given an integer N and an array of N integers. Calculate the sum of products of all pairs of integers of the array.
Note: Since the answer can be large, return the answer modulo 10^{9}+7.
Example 1:
Input:
N=3
A=[1,2,3]
Output:
11
Explanation:
1x2+2x3+1x3=11
So, the answer is 11.
Example 2:
Input:
N=3
A=[2,2,3]
Output:
16
Explanation:
2x2+2x3+3x2=16.
So, the answer is 16.
Your Task:
You don't need to read input or print anything. Your task is to complete the function productOfPairs() which takes the integer N and array A as input parameters and returns the sum of the product of all pairs of integers from the array.
Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)
 
Constraints:
1<=N,A[i]<=10^{6}
"""

def calculate_sum_of_products(N, A):
    MOD = 1000000007
    total = 0
    res = 0
    for i in range(N):
        res += total * A[i]
        res %= MOD
        total += A[i]
    return res