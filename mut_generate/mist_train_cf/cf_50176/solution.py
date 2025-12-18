"""
QUESTION:
Create a function `dessertCost(baseCosts, toppingCosts, toppingLimits, target)` that takes four inputs: 
- `baseCosts`, an integer array of length `n`, where each `baseCosts[i]` represents the price of the `ith` ice cream base flavor.
- `toppingCosts`, an integer array of length `m`, where each `toppingCosts[i]` is the price of one of the `ith` topping.
- `toppingLimits`, an integer array of length `m`, where each `toppingLimits[i]` is the maximum number of times the `ith` topping can be used.
- `target`, an integer representing your target price for dessert.

The function should return the closest possible cost of the dessert to `target`. If there are multiple, return the lower one.

Constraints: 
- `n == baseCosts.length`
- `m == toppingCosts.length`
- `m == toppingLimits.length`
- `1 <= n, m <= 10`
- `1 <= baseCosts[i], toppingCosts[i] <= 10^4`
- `1 <= toppingLimits[i] <= 10`
- `1 <= target <= 10^4`
"""

import bisect

def dessertCost(baseCosts, toppingCosts, toppingLimits, target):
    baseCosts.sort()
    toppingCosts.sort()
    result = baseCosts[0]
    m, n = len(baseCosts), len(toppingCosts)

    def dfs(i, total):
        nonlocal result
        if abs(result-target) >= abs(total-target):
            if abs(result-target) == abs(total-target):
                result = min(result, total)
            else:
                result = total
        if i == m or total-target >= abs(result-target):
            return
        dfs(i+1, total)
        for k in range(n):
            for _ in range(toppingLimits[k]):
                total += toppingCosts[k]
                if total - target > abs(result-target):
                    return
                dfs(i+1, total)
            total -= toppingLimits[k] * toppingCosts[k]

    dfs(0, 0)
    return result