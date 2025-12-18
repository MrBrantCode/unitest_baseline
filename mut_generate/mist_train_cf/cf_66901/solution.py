"""
QUESTION:
Find T(M) as the sum of all m ≤ 3^M for which Bob can guarantee winning the game, assuming optimal play, modulo 1,000,000,007, given that T(M) is the sum of all m for which Bob can guarantee victory by playing a number such that the ternary representation of 3m has an even number of digits.
"""

def T(M):
    MOD = 10**9 + 7
    pow3 = [1]
    while len(pow3) <= M:
        pow3.append(pow3[-1] * 3 % MOD)
    even = [0] * len(pow3)
    odd = [0] * len(pow3)
    even[0] = 1
    for i in range(len(pow3) - 1):
        even[i+1] = (even[i] + pow3[i] * odd[i]) % MOD
        odd[i+1] = (odd[i] + pow3[i] * even[i]) % MOD
    T = [0] * len(pow3)
    for i in range(len(pow3) - 1):
        T[i+1] = (3 * T[i] + pow3[i+1] * even[i+1]) % MOD
    return T[-1]