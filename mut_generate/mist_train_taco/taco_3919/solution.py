"""
QUESTION:
We already know Basic Euclidean Algorithm. Now using the Extended Euclidean Algorithm, given a and b calculate the GCD and integer coefficients x, y. Using the same. x and y must satisfy the equation ax + by = gcd(a, b) .
 
Example 1:
Input:
a = 35
b = 15
Output:
5 1 -2
Explanation:
gcd(a,b) = 5
35*1 + 15*(-2) = 5
Example 2:
Input:
a = 30
b = 20
Output:
10 1 -1
Explanation:
gcd(30,20) = 10
30*(1) + 20*(-1) = 10
Your Task:
You don't need to read input or print anything. Your task is to complete the function gcd() which takes an integer N as input parameters and returns array of three numbers containing gcd, x, y in the same order.
 
Expected Time Complexity: O(log max(a,b))
Expected Space Complexity: O(1)
 
Constraints:
1 <= a,b <= 10^{6}
"""

def extended_gcd(a: int, b: int) -> tuple:
    (r, r0) = (a, b)
    (s, s0) = (1, 0)
    (t, t0) = (0, 1)
    while r0 != 0:
        q = r // r0
        (r, r0) = (r0, r - q * r0)
        (s, s0) = (s0, s - q * s0)
        (t, t0) = (t0, t - q * t0)
    d = r
    return (d, s, t)