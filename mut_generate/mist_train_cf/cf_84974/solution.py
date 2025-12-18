"""
QUESTION:
Function `numberOfSubstrings(s)` where `s` is a binary string. Return the number of substrings with all characters 1's or all characters 0's modulo 10^9 + 7, and the number of substrings that contain an equal number of 1's and 0's. Constraints: `s[i] == '0'` or `s[i] == '1'`, and `1 <= s.length <= 10^5`.
"""

def numberOfSubstrings(s: str) -> list:
    MOD = 10 ** 9 + 7

    n = len(s)
    one_count = [0] * (n + 1)
    zero_count = [0] * (n + 1)

    for i in range(1, n + 1):
        if s[i - 1] == '1':
            one_count[i] = one_count[i - 1] + 1
            zero_count[i] = zero_count[i - 1]
        else:
           zero_count[i] = zero_count[i - 1] + 1
           one_count[i] = one_count[i - 1]

    equal_count = sum(min(z, o) for z, o in zip(zero_count, one_count))

    count_one = one_count[n] * (one_count[n] + 1) // 2  
    count_zero = zero_count[n] * (zero_count[n] + 1) // 2

    total = (count_one + count_zero - equal_count) % MOD

    return [total, equal_count]