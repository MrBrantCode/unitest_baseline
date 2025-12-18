"""
QUESTION:
Minimizing Deviation in Rounding to Achieve a Specific Sum

Create a function `minimizeRoundingError` that takes in an array of string prices and a target value. The function should round each price to either the floor or ceiling value such that the sum of the rounded prices equals the target. If it is not possible to achieve the target, return "-1". Otherwise, return the minimal rounding deviation as a string with three decimal places.

Constraints:

- The length of the prices array is between 1 and 500.
- Each string price represents a real number between 0.0 and 1000.0 with precisely 3 decimal places.
- The target value is between 0 and 10^6.
"""

import heapq

def minimizeRoundingError(prices, target):
    n, target, ceiling = len(prices), int(target), []
    prices = [float(p) for p in prices]
    flo = [int(p) for p in prices]
    F = sum(flo)
    for i in range(n):
        if flo[i] < prices[i]:
            heapq.heappush(ceiling, (flo[i]-prices[i], i))
    if target < F:
        return "-1"
    while F < target:
        F += 1
        i = heapq.heappop(ceiling)[1]
        flo[i] += 1
    ans = sum([abs(flo[i]-prices[i]) for i in range(n)])
    return '{:.3f}'.format(ans)