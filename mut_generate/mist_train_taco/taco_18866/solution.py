"""
QUESTION:
A number n is said to be a Carmichael number if it satisfies the following modular arithmetic condition:
  power(b, n-1) MOD n = 1, 
  for all b ranging from 1 to n such that b and 
  n are relatively prime, i.e, gcd(b, n) = 1 
Given a positive integer n, find if it is a Carmichael number.
Example 1:
Input: n = 8
Output: 0
Explaination: 3 is relatively prime to 
8 but 3^{(8 - 1)}%8 = 2187%8 != 1
Example 2:
Input: n = 3
Output: 1
Explaination: For both 1 and 2 the 
condition satisfied.
Your Task:
You do not need to read input or print anything. Your task is to complete the function isCarmichael() which takes n as input parameter and returns 1 if it is a carmichael number. Otherwise, returns 0.
Expected Time Complexity: O(n*Logn)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 100000
"""

import math

def binpow(a, b, n):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % n
        a = a * a % n
        b >>= 1
    return ans

def is_carmichael(n):
    for b in range(1, n + 1):
        if math.gcd(b, n) == 1 and binpow(b, n - 1, n) != 1:
            return 0
    return 1