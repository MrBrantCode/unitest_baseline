"""
QUESTION:
Given a polynomial represented as poly[] of size n and a value x, compute value of the polynomial for given x.  The result should be computed under modulo 10^{9}+7. 
Example 1:
Input: n = 4, x = 3
poly = {2, -6, 2, -1}
Output: 5
Explaination: Output is value of 2x^{3} - 6x^{2} + 
2x - 1 for x = 3.
Example 2:
Input: n = 4, x = 2
poly = {1, 2, 0, 4}
Output: 20
Explaination: Output is value of x^{3} + 2x^{2} + 4 
for x = 2.
Your Task:
You do not need to read input or print anything. Your task is to complete the function value() which takes n, poly and x as input parameters and returns the value of the polynomial modulo 10^{9} + 7.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 2000
-1000 ≤ poly[i] ≤ 1000
1 ≤ x ≤ 1000
"""

def compute_polynomial_value(n: int, poly: list[int], x: int) -> int:
    MOD = 1000000007
    result = 0
    for i in range(n):
        result += poly[i] * pow(x, n - i - 1, MOD)
        result %= MOD
    return result