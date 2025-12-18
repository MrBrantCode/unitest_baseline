"""
QUESTION:
Implement a function `rolling_hash` that takes a string `s` of length `n` (1 ≤ n ≤ 10^5), a prime number `p` (2 ≤ p ≤ 10^3), and a modulo value `m` (1 ≤ m ≤ 10^9) as input, and returns the hash value of the input string using the polynomial rolling hash function H(S) = ∑[S[i] × p^i] mod m, where S[i] is the ASCII value of the i-th character of the string.
"""

def rolling_hash(s, p, m):
    n = len(s)
    hash_value = 0
    for i in range(n):
        hash_value = (hash_value + ord(s[i]) * pow(p, i, m)) % m
    return hash_value