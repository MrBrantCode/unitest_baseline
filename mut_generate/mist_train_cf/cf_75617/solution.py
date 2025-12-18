"""
QUESTION:
Write a function named `count_combinations` that determines the quantity of distinct combinations available to create a change of `n` utilizing a specific set of coin denominations. The function should take two parameters: `coins` (a list of coin denominations) and `n` (the required change). The function should return the number of distinct combinations. Assume that the list of coins and the required change will always be non-negative integers.
"""

def count_combinations(coins, n):
    # Initialize the memo table
    memo = [0] * (n + 1)
    
    # Base case: there's only 1 combination when n = 0 (using no coins)
    memo[0] = 1
    
    # Iterate through each coin and update the memo table
    for coin in coins:
        for i in range(coin, n + 1):
            memo[i] += memo[i - coin]
    
    return memo[n]