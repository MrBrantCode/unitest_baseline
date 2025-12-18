"""
QUESTION:
Implement a function `greedy_knapsack` that solves the knapsack optimization problem using a greedy algorithm. The function should take in a list of items, each with a `name`, `value`, and `weight`, and the capacity of the knapsack. The function should return a list of the items in the knapsack and the total value of the items. The function should use a greedy approach, sorting the items by their value-to-weight ratio and then trying to fit them in the knapsack, starting from the item with the highest ratio.
"""

def greedy_knapsack(items, capacity):
    # Sort the items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x['value'] / x['weight'], reverse=True)

    # Initialize the total value of the knapsack
    total_value = 0

    # Initialize an empty list for the items in the knapsack
    knapsack = []

    # Try to fit each item in the knapsack
    for item in items:
        if item['weight'] <= capacity:
            # If the item fits in the knapsack, add it
            knapsack.append(item['name'])
            total_value += item['value']
            capacity -= item['weight']

    # Return the items in the knapsack and the total value
    return knapsack, total_value