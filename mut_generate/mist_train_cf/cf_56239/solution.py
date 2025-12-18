"""
QUESTION:
Given a unique set of coin denominations and a target sum, create a function `minCoins(coins, sum)` that returns the minimal quantity of coins needed to reach the target sum using the available denominations. If no combination of denominations can form the given sum, return -1. The function should have a time complexity of O(n*sum) and space complexity of O(sum), where n is the number of coins and sum is the target sum.
"""

def minCoins(coins, sum):
  min_coins = [float('inf')] * (sum + 1) 
  min_coins[0] = 0 # base case
  
  for denom in coins:
      for i in range(denom, sum + 1):
          min_coins[i] = min(min_coins[i], 1 + min_coins[i-denom])

  return min_coins[sum] if min_coins[sum] != float('inf') else -1