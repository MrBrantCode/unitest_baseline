"""
QUESTION:
Given a Geometric Progression with first term as 1, common ratio as 2 and a number N. Find out the sum of all the terms of this geometric progression if there are total 2^{N} terms in GP.
Note: Since the answer can be very large, print the answer modulo 10^{9}+7.
 
Example 1:
Input:
N = 1
Output:
3
Explanation:
The series = 1,2. Sum = 1+2 = 3.
Example 2:
Input:
N = 2
Output:
15
Explanation:
The series = 1,2,4,8. Sum = 1+2+4+8 = 15.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function geoProg() which takes a Integer N as input and returns the sum of all the terms of this geometric progression if there are total 2^{N} terms in GP modulo (10^{9}+7).
 
Expected Time Complexity: O((log(N))^{2})
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{18}
"""

def sum_of_geometric_progression(N: int) -> int:
    MOD = 10**9 + 7
    return (pow(2, pow(2, N, MOD - 1), MOD) - 1 + MOD) % MOD