"""
QUESTION:
Implement a function `getNumberOfBacklogOrders` that takes a 2D integer array `orders` where each `orders[i] = [timei, amounti, orderTypei]`. Return the total amount of orders in the queue after placing all the orders from the input modulo 10^9 + 7. 

The orderTypei is 0 for buy orders and 1 for sell orders. The function should follow the given matching and execution rules for the orders. The input array `orders` has a length of at least 1 and at most 10^5, and each `orders[i]` has exactly 3 elements. The timei and amounti are both between 1 and 10^9 inclusive, and orderTypei is either 0 or 1.
"""

import heapq

def getNumberOfBacklogOrders(orders):
    buys, sells, mod = [], [], 1_000_000_007
    for time, amount, is_sell in sorted(orders):
        queue, opposite = (sells, buys) if is_sell else (buys, sells)
        while amount > 0 and opposite and (is_sell == (opposite[-1][0] <= time)):
            otime, oamount = heapq.heappop(opposite)
            deal = min(amount, oamount)
            amount -= deal
            oamount -= deal
            if oamount != 0:
                heapq.heappush(opposite, (otime, oamount))
        if amount > 0:
            heapq.heappush(queue, (time if is_sell else -time, amount))
    return sum(amount for time, amount in buys + sells) % mod