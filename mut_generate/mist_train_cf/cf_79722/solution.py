"""
QUESTION:
Given a number of individuals `n`, a minimum value `minValue`, and two arrays `group` and `value` of the same length, where `group[i]` is the number of individuals required to decipher the `i`th code and `value[i]` is the value yielded by deciphering the `i`th code, write a function `enigmaticCodes(n, minValue, group, value)` to determine the number of codes that can be successfully deciphered to produce a value equal to or exceeding `minValue` with the total number of individuals not exceeding `n`. Return the result modulo `10^9 + 7`. The function should take into account that an individual, once engaged in the decryption of a code, cannot decipher another.

Constraints: 
`1 <= n <= 100`
`0 <= minValue <= 100`
`1 <= len(group) <= 100`
`1 <= group[i] <= 100`
`len(value) == len(group)`
`0 <= value[i] <= 100`
"""

def enigmaticCodes(n, minValue, group, value):
    MOD = int(1e9+7)
    dp = [[0]*(n+1) for _ in range(sum(value) + 1)]
    dp[0][0] = 1
    for k in range(len(group)):
        for i in range(sum(value),value[k]-1,-1):
            for j in range(n,group[k]-1,-1):
                dp[i][j] = (dp[i][j] + dp[i - value[k]][j - group[k]])%MOD
        
    return sum(dp[i][j] for i in range(minValue, sum(value) + 1) for j in range(n + 1))%MOD