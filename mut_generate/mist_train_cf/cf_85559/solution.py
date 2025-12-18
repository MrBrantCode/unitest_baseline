"""
QUESTION:
Find `F(N)`, where `F(N) = ∑[lcm(i,j) for i in range(1, j+1) for j in range(1, N+1)]`, given `F(10) = 420`. Calculate `F(10^11)` modulo `1000000007`.
"""

import math

def entrance(N):
    MOD = 1000000007
    sum_ = 0
    for j in range(1, N+1):
        lcm_sum = sum([math.gcd(j, i)*i for i in range(1, j+1)]) % MOD
        sum_ = (sum_+(lcm_sum*j)) % MOD
    return sum_