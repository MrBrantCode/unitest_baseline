"""
QUESTION:
Write a Python function named `knapsack_greedy` that implements the greedy algorithm for the 0/1 knapsack problem. The function should take a list of items where each item is represented as a tuple `(weight, value)`, and a maximum capacity `capacity` as input, and return a list of the selected items. The function should prioritize items based on their value-to-weight ratio and should not exceed the given capacity.
"""

def knapsack_greedy(items, capacity):
    """
    A greedy algorithm for the 0/1 knapsack problem.

    Parameters:
    items (list): A list of items where each item is represented as a tuple (weight, value)
    capacity (int): The maximum capacity of the knapsack

    Returns:
    list: A list of the selected items
    """
    # Calculate the value-to-weight ratio for each item and store it as a tuple along with the item
    ratios = [(value / weight, weight, value) for weight, value in items]
    
    # Sort the items based on their value-to-weight ratio in descending order
    ratios.sort(reverse=True)
    
    # Initialize the selected items and the remaining capacity
    selected_items = []
    remaining_capacity = capacity
    
    # Iterate over the sorted items
    for ratio, weight, value in ratios:
        # If the item fits in the remaining capacity, add it to the selected items
        if weight <= remaining_capacity:
            selected_items.append((weight, value))
            remaining_capacity -= weight
    
    return selected_items