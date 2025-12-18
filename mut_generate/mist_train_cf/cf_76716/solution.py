"""
QUESTION:
Determine the number of "reward" sequences that would exist over a span of n days, where a reward sequence is a sequence of 'O', 'L', and 'A' that does not contain three consecutive 'A's or more than one 'L'. A student's attendance record is a sequence of 'O', 'L', and 'A', where 'O' denotes on-time arrival, 'L' denotes lateness, and 'A' denotes absence. The function checkRecord should take an integer n as input and return the number of reward sequences of length n.
"""

def checkRecord(n):
    dp = [[[[0, 0] for _ in range(3)] for __ in range(2)] for ___ in range(n+1)]
    
    MOD = 10**9 + 7
    dp[0][0][0][0] = 1

    for i in range(n):
        for a in range(2):                  
            for l in range(3):              
                for k in range(2):          
                    val = dp[i][a][l][k]
                    dp[i+1][a][0][k] = (dp[i+1][a][0][k] + val) % MOD
                    if l < 2:
                        dp[i+1][a][l+1][k] = (dp[i+1][a][l+1][k] + val) % MOD
                    if a < 1:
                        dp[i+1][a+1][0][1-k] = (dp[i+1][a+1][0][1-k] + val) % MOD

    ans = 0
    for a in range(2):
        for l in range(3):
            for k in range(2):
                ans = (ans + dp[n][a][l][k]) % MOD

    return ans