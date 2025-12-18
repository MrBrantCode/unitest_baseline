"""
QUESTION:
Implement a function `fractional_knapsack` that takes two lists `values` and `weights` representing the values and weights of items respectively, and an integer `capacity` representing the maximum weight capacity of a knapsack. Return the maximum total value that can be put in a knapsack, allowing for fractional values.
"""

def fractional_knapsack(values, weights, capacity):
    """
    This function calculates the maximum total value that can be put in a knapsack, 
    allowing for fractional values.

    Args:
    values (list): A list of values of items.
    weights (list): A list of weights of items.
    capacity (int): The maximum weight capacity of a knapsack.

    Returns:
    float: The maximum total value that can be put in a knapsack.
    """
    # Combine values and weights into a list of tuples and calculate value-to-weight ratio
    items = [(value / weight, value, weight) for value, weight in zip(values, weights)]
    
    # Sort the items in descending order based on their value-to-weight ratio
    items.sort(reverse=True)
    
    total_value = 0.0
    for ratio, value, weight in items:
        # If the weight of the current item is less than or equal to the remaining capacity, 
        # add the entire item to the knapsack
        if weight <= capacity:
            capacity -= weight
            total_value += value
        # If the weight of the current item is greater than the remaining capacity, 
        # add a fraction of the item to the knapsack
        else:
            fraction = capacity / weight
            total_value += value * fraction
            break
    
    return total_value