"""
QUESTION:
Given an integer n, write a function checkRecord that computes the number of possible attendance records of length n that would make a student eligible for an attendance award, with the following rules:

- The student's total absences ('A') are less than 2 days.
- The student has not been late ('L') for 3 or more consecutive days.

Return the result modulo 10^9 + 7.

Constraints: 1 <= n <= 10^5
"""

def checkRecord(n):
    mod = 10**9 + 7
    dp = [[0, 0, 0] for _ in range(n+1)]
    dp[0] = [1, 1, 0]
    dp[1] = [2, 2, 1]

    for i in range(2, n+1):
        dp[i][0] = sum(dp[i-1]) % mod
        dp[i][1] = (dp[i][0]+dp[i-1][1]) % mod
        dp[i][2] = (dp[i][1]+dp[i-1][2]) % mod

    return (sum(dp[-1])*2-dp[-1][0]) % mod