"""
QUESTION:
Stone Game III: 

Given an array `stoneValue` representing the values of stones in a row, determine the winner of a game where two players, Alice and Bob, take turns removing 1, 2, or 3 stones from the front of the row. The score of each player is the sum of the values of the stones they remove. If Alice plays optimally, determine if she will win, lose, or tie against Bob, who also plays optimally.

Function: `stoneGameIII(stoneValue)`

Restrictions: `1 <= stoneValue.length <= 50000` and `-1000 <= stoneValue[i] <= 1000`.
"""

def stoneGameIII(stoneValue):
    n = len(stoneValue)
    dp, sumi = [0] * (n + 1), [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(sumi[i + k] - dp[i + k] for k in range(1, min(4, n - i + 1)))
        sumi[i] = sumi[i + 1] + stoneValue[i]
    if dp[0] > sumi[0] - dp[0]:
        return "Alice"
    elif dp[0] == sumi[0] - dp[0]:
        return "Tie"
    else:
        return "Bob"