"""
QUESTION:
Write a function `ways_to_construct(amount, coins)` that calculates the total count of distinct methods to construct a given amount using the provided coin denominations. The function takes two parameters: `amount` (the target sum in pence) and `coins` (a list of coin denominations in pence). The function should return the total count of distinct methods. The available coins are 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
"""

def ways_to_construct(amount, coins): 
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]