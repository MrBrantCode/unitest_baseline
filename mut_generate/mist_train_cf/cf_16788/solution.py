"""
QUESTION:
Implement a function `knapsack_fractional` that takes as input a list of items, where each item is a tuple `(weight, value, quantity)`, a knapsack capacity `capacity`, and a maximum quantity limit `k` for each item. The function should return the maximum total value that can be achieved without exceeding the capacity and the maximum quantity limit for each item.
"""

def knapsack_fractional(items, capacity, k):
    # Sort items by their value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    total_weight = 0

    for weight, value, quantity in sorted_items:
        max_quantity = min(k, quantity, capacity // weight)
        
        if max_quantity > 0:
            total_value += value * max_quantity
            total_weight += weight * max_quantity
            capacity -= weight * max_quantity
            k -= max_quantity

            if capacity == 0 or k == 0:
                break

        if max_quantity < quantity:
            remaining_capacity = capacity
            remaining_quantity = k
            fractional_quantity = min(remaining_capacity / weight, remaining_quantity)
            total_value += value * fractional_quantity
            total_weight += weight * fractional_quantity
            capacity -= weight * fractional_quantity
            k -= fractional_quantity

    return total_value