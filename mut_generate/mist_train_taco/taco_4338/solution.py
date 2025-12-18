"""
QUESTION:
Given four numbers X, Y, Z and N. Find smallest N digit Number that is divisible by all the three numbers X, Y and Z.
Example 1:
Input: 
N = 2
X = 2, Y = 3, Z = 5
Output: 30
Explaination: 30 is the lcm of 2, 3 and 5 
and it is a 2 digit number.
Example 2:
Input: 
N = 2
X = 3, Y = 5, Z = 7
Output: -1
Explaination: There is no 2 digit number 
divisible by 3, 5 and 7.
Your Task:
You do not need to read input or print anything. Your task is to complete the function minNumber() which takes the four number X, Y, Z and N as input parameters and returns the smallest N digit number divisible by X, Y and Z. If ther is no such number, return -1.
Expected Time Complexity: O(Log X)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ X, Y, Z, ≤ 1000
1 ≤ N ≤ 18
"""

import math

def find_smallest_n_digit_divisible(X: int, Y: int, Z: int, N: int) -> int:
    def lcm(x, y, z):
        ans = x * y // math.gcd(x, y)
        return z * ans // math.gcd(ans, z)
    
    maxx = pow(10, N - 1)
    lcm_value = lcm(X, Y, Z)
    rem = maxx % lcm_value
    
    if rem == 0:
        return maxx
    
    if lcm_value > pow(10, N):
        return -1
    
    ans = maxx + (lcm_value - rem)
    return ans