"""
QUESTION:
Write a function `twoCitySchedCost` that takes a 2D array `costs` as input, where `costs[i] = [aCosti, bCosti]` represents the expense of transporting the ith candidate to metropolis A and B respectively. The function should return the least possible expense to transport each candidate to a metropolis, ensuring that precisely half of the candidates reach each metropolis. The length of `costs` is even, and 2 <= `costs.length` <= 100.
"""

def twoCitySchedCost(costs):
    sorted_costs = sorted(costs, key = lambda x : x[0] - x[1])
    total = 0
    n = len(costs) // 2
    for i in range(n):
        total += sorted_costs[i][0] + sorted_costs[i+n][1]
    return total