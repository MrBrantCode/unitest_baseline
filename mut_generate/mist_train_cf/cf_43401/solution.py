"""
QUESTION:
Write a function `calcExponentialGrowth(P, r, transactions, m)` that calculates the total value of an investment at a given time `m` with an initial principal `P`, annual interest rate `r`, and a list of transactions. Each transaction is a tuple of `(timestamp, investment_value)` and the list is sorted by timestamp in ascending order. The function should handle both the compounded growth of the investment and the addition of new investments over time, returning the total value at time `m`. The function should also work correctly when the list of transactions is empty, in which case it should behave as a simple continuously compounded interest calculator.
"""

import math

def calcExponentialGrowth(P, r, transactions, m):
    total = P
    last_t = 0
    for tx in transactions:
        t, P_tx = tx
        delta_t = t - last_t
        total = total * math.exp(r*delta_t) + P_tx
        last_t = t
    total = total * math.exp(r * (m - last_t))
    return total