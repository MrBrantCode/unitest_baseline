"""
QUESTION:
Given an integer n, implement a function `knightDialer` that returns how many distinct phone numbers of length n can be dialed using a chess knight on a phone pad, with the restriction that the phone number cannot contain any repeated consecutive digits. The knight can only stand on a numeric cell initially and then perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps. Return the answer modulo 10^9 + 7.

The function should take an integer n as input, where 1 <= n <= 5000.
"""

def knightDialer(n: int) -> int:
    phone = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]
    dp = [1] * 10
    for i in range(n - 1):
        dp2 = [0] * 10
        for j in range(10):
            for k in phone[j]:
                dp2[k] += dp[j]
                dp2[k] %= (10**9 + 7)
        dp = dp2
    return sum(dp) % (10**9 + 7)