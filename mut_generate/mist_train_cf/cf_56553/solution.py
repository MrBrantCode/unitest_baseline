"""
QUESTION:
You are given the prices of different items, a set of special offers where each offer consists of one or more different kinds of items with a sale price and a limit on the number of times it can be used, and the number of each item you need to buy. Find the lowest price you have to pay for exactly the given items, where you can use the special offers as many times as possible within their usage limits. 

Each special offer is represented as a list where the last number is the price and the other numbers represent how many specific items you get with the offer. The function `shoppingOffers(price, special, needs)` should return the minimum cost. The prices, special offers, and needs are all lists of integers. 

Restrictions: There are at most 6 kinds of items, 100 special offers, each item can be bought at most 6 times, and each special offer can be used at most 10 times.
"""

import sys

def shoppingOffers(price, special, needs):
    dp = {}

    def dfs(needs):
        needs = tuple(needs)
        if needs in dp:
            return dp[needs]
        
        cost = sum(needs[i] * price[i] for i in range(len(needs)))
        
        for offer in special:
            if all(needs[i] >= offer[i] for i in range(len(needs))):
                new_needs = [needs[i] - offer[i] for i in range(len(needs))]
                cost = min(cost, dfs(new_needs) + offer[-1])
                
        dp[needs] = cost
        return cost

    ans = dfs(needs)
    return ans if ans != float('inf') else -1