"""
QUESTION:
Implement a function called `greedy_algorithm` that takes in a list of items and a capacity. Each item is a tuple of (value, cost, weight). The function should return a list where each element is 1 if the item is selected, and 0 if it is not. The function should select items based on their weights, choosing the ones that fit within the given capacity, without considering future steps or the global optimum solution.
"""

def greedy_algorithm(items, capacity):
    result = [0] * len(items)
    items.sort(key=lambda x: x[2])
    for i in range(len(items)):
        if items[i][2] <= capacity:
            result[i] = 1
            capacity -= items[i][2]
    return result