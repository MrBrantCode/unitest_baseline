"""
QUESTION:
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:


Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.


Example 2:


Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

import heapq

def max_profit_with_k_transactions(prices, k):
    length = len(prices)
    v = p = 0
    pairs = []
    profits = []
    
    while p < length:
        v = p
        while v < length - 1 and prices[v] >= prices[v + 1]:
            v += 1
        p = v + 1
        while p < length and prices[p] >= prices[p - 1]:
            p += 1
        
        while pairs and prices[v] < prices[pairs[-1][0]]:
            heapq.heappush(profits, prices[pairs[-1][0]] - prices[pairs[-1][1] - 1])
            pairs.pop()
        
        while pairs and prices[p - 1] >= prices[pairs[-1][1] - 1]:
            heapq.heappush(profits, prices[v] - prices[pairs[-1][1] - 1])
            v = pairs[-1][0]
            pairs.pop()
        
        pairs.append((v, p))
    
    while pairs:
        heapq.heappush(profits, prices[pairs[-1][0]] - prices[pairs[-1][1] - 1])
        pairs.pop()
    
    ans = 0
    while k != 0 and profits:
        ans += -heapq.heappop(profits)
        k -= 1
    
    return ans