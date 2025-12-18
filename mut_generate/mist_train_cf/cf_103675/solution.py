"""
QUESTION:
Write a function named `calculate_cost` that takes two parameters: the number of items (`X`) and the cost per item. The function should return the total cost of purchasing `X` items at the given cost per item, but only if the cost per item is within the range of 1.00 to 10.00 (inclusive). If the cost per item is outside this range, the function should return an error message.
"""

def calculate_cost(X, cost):
    if cost < 1.00 or cost > 10.00:
        return "Invalid cost per item! Please provide a cost between 1.00 and 10.00."
    total_cost = X * cost
    return total_cost