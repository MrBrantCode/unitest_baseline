"""
QUESTION:
Create a function `fractional_knapsack(value, weight, capacity)` that takes in three parameters: `value` and `weight` lists representing the value and weight of each item respectively, and an integer `capacity` representing the maximum weight the knapsack can hold. The function should return the maximum possible value that can be put in a knapsack of the given capacity using the fractional knapsack problem greedy algorithm.
"""

def fractional_knapsack(value, weight, capacity):
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    
    index.sort(key = lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(value)
    
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break

    return max_value