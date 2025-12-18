"""
QUESTION:
Write a function `minCoins(coins, m, V)` that determines the least number of coins required to achieve a specific total monetary value `V` using a distinct collection of coin denominations `coins`. The function should take in three parameters: `coins` (a list of coin denominations), `m` (the number of coin denominations), and `V` (the total monetary value). The function should return the minimum number of coins required to achieve the total monetary value `V`.
"""

def minCoins(coins, m, V):
    # table[i] will be storing the minimum
    #  number of coins required for i value.
    table = [0] + [float('inf')] * V
 
    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V+1):
 
        # Go through all coins smaller than i
        for coin in coins:
            if (coin <= i):
                sub_res = table[i - coin]
                if (sub_res != float('inf') and
                   sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
 
    return table[V]