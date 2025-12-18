"""
QUESTION:
Given a string `s` and an array of integers `cost` where `cost[i]` is the cost of deleting the `i-th` character in `s`, write a function `minCost(s, cost, k)` that returns the minimum cost of deletions such that there are no two identical letters next to each other, given that the maximum number of deletions allowed is `k`. If it's not possible to satisfy the condition with `k` deletions, return -1. The length of `s` and `cost` is between 1 and 10^5, and the values in `cost` are between 1 and 10^4. `s` contains only lowercase English letters. The function should run in O(N) time complexity and use O(1) space complexity.
"""

def minCost(s, cost, k):
    n = len(s)
    totalCost, maxCost, count = 0, 0, 0
    for i in range(n):
        if i > 0 and s[i] != s[i-1]:
            k -= count - 1
            if k < 0:
                return -1
            totalCost -= maxCost
            count = 0
            maxCost = 0
        totalCost += cost[i]
        maxCost = max(maxCost, cost[i])
        count += 1
    
    k -= count - 1
    if k < 0:
        return -1
    totalCost -= maxCost        
    return totalCost