"""
QUESTION:
You are given an array `inventory` representing the quantity of each colored ball you own and an integer `orders` representing the total number of balls to sell. The value of each ball is equivalent to the current quantity of that color in your inventory. Your task is to write a function `maxProfit` that determines the maximum total value you can achieve after selling `orders` colored balls and return it modulo `10^9 + 7`. The function should take `inventory` and `orders` as input and return the result.

Constraints:
- `1 <= inventory.length <= 10^5`
- `1 <= inventory[i] <= 10^9`
- `1 <= orders <= min(sum(inventory[i]), 10^9)`
"""

import heapq

def maxProfit(inventory, orders):
    MOD = 10**9 + 7
    inventory = [-1*a for a in inventory]
    heapq.heapify(inventory)
    max_profit = 0
    while orders > 0:
        cur_val = -1*heapq.heappop(inventory)
        if len(inventory) > 0:
            next_val = -1*inventory[0]
        else:
            next_val = 0
        n_to_reduce = min(orders, cur_val-next_val+1)
        total, r = divmod(n_to_reduce, cur_val-next_val+1)
        max_profit += (total*(cur_val+cur_val-total+1))//2*(cur_val-next_val+1) + r*(cur_val-total)
        max_profit %= MOD
        heapq.heappush(inventory, -1*(cur_val - total - 1))
        orders -= n_to_reduce
    return max_profit