"""
QUESTION:
Given two integers n and k, The task is to calculate Permutation Coefficient P(n,k)
Note: P(n, k) is used to represent the number of ways to obtain an ordered subset having k elements from a set of n elements.Since this value may be large only find it modulo 10^9 + 7.
Example 1:
Input: n = 10, k = 2
Output: 90
Explanation: For first case:
Ans = 10! / (10 - 2)! = 10! / 8!
10! is 8!*9*10 and 8! is 8!
Ans = 9*10 = 90
Example 2:
Input: n = 10, k = 3
Output: 720
Your Task:
You don't need to read or print anything. Your task is to complete the function permutationCoeff() which takes integers n and kas input parameters and returns an integer.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
 
Constraints:
1 ≤ k ≤ n ≤ 100000
"""

def permutation_coefficient(n: int, k: int) -> int:
    MOD = 10**9 + 7
    result = 1
    for i in range(n, n - k, -1):
        result = (result * i) % MOD
    return result