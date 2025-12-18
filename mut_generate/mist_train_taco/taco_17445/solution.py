"""
QUESTION:
Given an integer N. Integers A and B are chosen randomly in the range [1..N]. Calculate the probability that the Greatest Common Divisor(GCD) of A and B equals to B.

-----Input-----
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case consists of a single integer N on a separate line.

-----Output-----
For each test case, output a single line containing probability as an irreducible fraction. 

-----Example-----
Input:
3
1
2
3

Output:
1/1
3/4
5/9

-----Constraints-----

1<=T<=103

1<=N<=109
"""

import math

def calculate_gcd_probability(N):
    ans = 0
    x = math.floor(math.sqrt(N))
    i = 1
    while i <= x:
        ans += N // i
        i += 1
    ans *= 2
    ans -= x ** 2
    num = int(ans)
    den = N * N
    g = math.gcd(num, den)
    return (num // g, den // g)