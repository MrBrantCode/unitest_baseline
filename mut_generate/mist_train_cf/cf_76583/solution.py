"""
QUESTION:
Create a function `coinChange(coins, amount)` that returns the fewest number of coins that need to make up the `amount` using the given `coins` of different denominations. If the amount cannot be made up by any combination of the coins, return `-1`. The function should also return the specific combination of coins used. 

The function should take an integer array `coins` and an integer `amount` as inputs. It is assumed that there is an infinite number of each kind of coin. The length of the `coins` array is between 1 and 12, each coin value is between 1 and 2^31 - 1, and the `amount` is between 0 and 10^4.
"""

def coinChange(coins, amount):
    MAX = float('inf')
    dp = [0] + [MAX] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

    # If no combination can sum to amount
    if dp[amount] == MAX:
        return -1, []
    
    # Backtracking to find the combination
    ans = []
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                ans.append(coin)
                amount -= coin
                break
                
    return dp[-1], ans