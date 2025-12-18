"""
QUESTION:
Calculate F(m, n) which denotes the count of the unique multiplicative outcomes of n positive integers that do not surpass m. The function F(m, n) should return this count modulo 1,000,000,007.

Here, m and n are positive integers. The result should be calculated using the formula for combinations, C(n+m-1, n), modulo 1,000,000,007.
"""

MOD = 1_000_000_007

# Precompute factorials upto n + m
factorial = [1]
for i in range(1, 30 + 10001 + 1):
    factorial.append((factorial[-1] * i) % MOD)

# Function to compute a^b mod MOD
def power(a, b, mod):
    res = 1
    while b:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def calculate_F(m, n):
    return (factorial[n + m] * power((factorial[m] * factorial[n]) % MOD, MOD - 2, MOD)) % MOD