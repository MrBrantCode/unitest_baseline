"""
QUESTION:
Madoka wants to enter to "Novosibirsk State University", but in the entrance exam she came across a very difficult task:

Given an integer $n$, it is required to calculate $\sum{\operatorname{lcm}(c, \gcd(a, b))}$, for all triples of positive integers $(a, b, c)$, where $a + b + c = n$.

In this problem $\gcd(x, y)$ denotes the greatest common divisor of $x$ and $y$, and $\operatorname{lcm}(x, y)$ denotes the least common multiple of $x$ and $y$.

Solve this problem for Madoka and help her to enter to the best university!


-----Input-----

The first and the only line contains a single integer $n$ ($3 \le n \le 10^5$).


-----Output-----

Print exactly one interger — $\sum{\operatorname{lcm}(c, \gcd(a, b))}$. Since the answer can be very large, then output it modulo $10^9 + 7$.


-----Examples-----

Input
3
Output
1
Input
5
Output
11
Input
69228
Output
778304278


-----Note-----

In the first example, there is only one suitable triple $(1, 1, 1)$. So the answer is $\operatorname{lcm}(1, \gcd(1, 1)) = \operatorname{lcm}(1, 1) = 1$.

In the second example, $\operatorname{lcm}(1, \gcd(3, 1)) + \operatorname{lcm}(1, \gcd(2, 2)) + \operatorname{lcm}(1, \gcd(1, 3)) + \operatorname{lcm}(2, \gcd(2, 1)) + \operatorname{lcm}(2, \gcd(1, 2)) + \operatorname{lcm}(3, \gcd(1, 1)) = \operatorname{lcm}(1, 1) + \operatorname{lcm}(1, 2) + \operatorname{lcm}(1, 1) + \operatorname{lcm}(2, 1) + \operatorname{lcm}(2, 1) + \operatorname{lcm}(3, 1) = 1 + 2 + 1 + 2 + 2 + 3 = 11$
"""

from math import gcd

def calculate_sum_lcm_gcd(n, MOD=10**9 + 7):
    # Precompute Euler's Totient function values
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] * (i - 1) // i
    
    # Precompute prefix sums of phi and phi * i
    P = [0, 0]
    Q = [0, 0]
    for i in range(2, n + 1):
        P.append((P[-1] + phi[i]) % MOD)
        Q.append((Q[-1] + phi[i] * i) % MOD)
    
    # Calculate the total sum
    tot = 0
    for g in range(1, n):
        c = n // g
        tot += n * g * P[c] // gcd(n, g) % MOD
        tot -= g * g * Q[c] // gcd(n, g) % MOD
    
    return tot % MOD