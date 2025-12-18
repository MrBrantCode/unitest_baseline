"""
QUESTION:
Write a function named `maxScore` that takes two lists, `scores` and `ages`, as input where `scores[i]` and `ages[i]` represent the score and age of the `ith` player, respectively. The function should return the maximum cumulative score that can be achieved by a team without conflicts, where a conflict occurs when a younger player has a score strictly superior to an older player. The length of `scores` and `ages` is between 1 and 1000 (inclusive), and the values in `scores` and `ages` are also between 1 and 10^6 (inclusive) and between 1 and 1000 (inclusive), respectively.
"""

def maxScore(scores, ages):
    n = len(scores)
    players = list(zip(ages, scores))
    players.sort()  
    dp = [0]*n 
    dp[0] = players[0][1]
    for i in range(1,n):
        dp[i] = players[i][1]
        for j in range(i):
            if players[i][1] >= players[j][1]:
                dp[i] = max(dp[i], dp[j] + players[i][1])
    return max(dp)