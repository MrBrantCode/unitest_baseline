"""
QUESTION:
Given a list of integers `coins` representing the values of coins and an integer `target` representing the target value, write a function `count_coin_combinations(coins: List[int], target: int) -> int` to determine the number of ways to make up the target value using the given coins with unlimited usage of each coin. Return the result modulo 10^9 + 7.
"""

def count_coin_combinations(coins, target):
    MOD = 10**9 + 7
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = (dp[i] + dp[i - coin]) % MOD

    return dp[target]