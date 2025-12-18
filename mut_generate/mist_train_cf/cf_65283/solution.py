"""
QUESTION:
Implement a function `fractional_knapsack(value, weight, capacity)` to solve the fractional knapsack problem. The function should take in three parameters: a list of item values `value`, a list of item weights `weight`, and the maximum capacity of the knapsack `capacity`. It should return a tuple containing the maximum total value of items that can be put in the knapsack and a list of fractions of each item to be taken, with the items prioritized by their value-to-weight ratio in descending order.
"""

def fractional_knapsack(value, weight, capacity):
    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    """
 
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
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
 
    return max_value, fractions