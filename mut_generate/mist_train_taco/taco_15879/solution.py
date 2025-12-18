"""
QUESTION:
Given 4 integers A, B, C and N, find the value of F(N) such that
F(1) = A + B 
F(2) = B + C 
F(N) = F(N-1) - F(N-2),  for N > 2. 
 
Example 1:
Input: N = 2, A = 2, B = 3, C = 4
Output: 7
Explaination: F(2) = B+C = 3+4 = 7
Example 2:
Input: N = 3, A = 2, B = 3, C = 4
Output: 2
Explaination: F(3) = F(2)- F(1) = 7-5 = 2
Your Task:
You do not need to read input or print anything. Your task is to complete the function modifiedFib() which takes the values N, A, B and C as input parameters and returns F(N). Since F(N) modulo (10^{9}+7).
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{12}
1 ≤ A, B, C ≤ 10^{9}
"""

def modified_fib(N, A, B, C):
    MOD = 1000000007
    (a, b, c) = (A + B, B + C, C - A)
    n = N % 6
    if n == 1:
        return a % MOD
    if n == 2:
        return b % MOD
    if n == 3:
        return c % MOD
    if n == 4:
        return -a % MOD
    if n == 5:
        return -b % MOD
    if n == 0:
        return -c % MOD