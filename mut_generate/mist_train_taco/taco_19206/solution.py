"""
QUESTION:
Implement pow(x, n) % M.
In other words, given x, n and M, find (x^{n}) % M.
 
Example 1:
Input:
x = 3, n = 2, m = 4
Output:
1
Explanation:
3^{2} = 9. 9 % 4 = 1.
Example 2:
Input:
x = 2, n = 6, m = 10
Output:
4
Explanation:
2^{6} = 64. 64 % 10 = 4.
Your Task:
You don't need to read or print anything. Your task is to complete the function PowMod() which takes integers x, n and M as input parameters and returns x^{n} % M.
 
Expected Time Complexity: O(log(n))
Expected Space Complexity: O(1)
 
Constraints:
1 ≤ x, n, M ≤ 10^{9}
"""

def pow_mod(x: int, n: int, m: int) -> int:
    res = 1
    while n > 0:
        if n & 1 != 0:
            res = res * x % m
        x = x * x % m
        n = n >> 1
    return res