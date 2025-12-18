"""
QUESTION:
Flip String to Monotone Increasing with Constraints

Create a function called `minFlipsMonoIncr` that takes a string `S` of '0's and '1's as input. The string is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0). Return the minimum number of flips to make `S` monotone increasing. The constraint is that a digit can be flipped if it is not adjacent to a digit of the same value.

The string `S` has a length between 1 and 20,000 (inclusive) and only consists of '0' and '1' characters.
"""

def minFlipsMonoIncr(S: str) -> int:
    n = len(S)
    no_of_zeros = S.count('0')
    no_of_ones = n - no_of_zeros
    dp = [0] * (n+1)
    min_flips = no_of_zeros
    ones_left = 0
    zeros_left = no_of_zeros
    for i in range(1, n+1):
        if S[i-1] == '0':
            zeros_left -= 1
        else:
            ones_left += 1
        dp[i] = min(ones_left + zeros_left, dp[i-1] + (1 if S[i-1] == '1' else 0))
        if dp[i] < min_flips:
            min_flips = dp[i]
    return min_flips