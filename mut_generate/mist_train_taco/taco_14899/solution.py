"""
QUESTION:
Given an integer N. Your task is to find the number of binary strings of length N having no consecutive 1s.
As the number can be large, return the answer modulo 10^9+7.
Example 1:
Input:
N = 3
Output:
5
Explanation:
All the binary strings of length 3 having
no consecutive 1s are "000", "001", "101",
"100" and "010".
Example 2:
Input: 
N = 2
Output:
3
Explanation: 
All the binary strings of length 2 having no 
consecutive 1s are "10", "00" and "01".
Your Task:
You dont need to read input or print anything. Complete the function countStrings() which takes the integer N as the input parameter, and returns the number of binary strings of length N with no consecutive 1s.
Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(Height of the recursive call stack)
Constraints:
1 ≤ N ≤ 10^{18}
"""

from functools import lru_cache

def count_binary_strings_no_consecutive_ones(N: int) -> int:
    MOD = 10**9 + 7
    
    @lru_cache(None)
    def recSol(n):
        if n == 1:
            return (1, 0, 0, 1)
        (a1, b1, c1, d1) = recSol(n // 2)
        (a2, b2, c2, d2) = recSol(n - n // 2)
        a3 = a1 * (a2 + c2) + b1 * a2
        b3 = a1 * (b2 + d2) + b1 * b2
        c3 = c1 * (a2 + c2) + d1 * a2
        d3 = c1 * (b2 + d2) + d1 * b2
        a3 %= MOD
        b3 %= MOD
        c3 %= MOD
        d3 %= MOD
        return (a3, b3, c3, d3)
    
    return sum(recSol(N)) % MOD