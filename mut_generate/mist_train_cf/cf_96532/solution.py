"""
QUESTION:
Write a function named `calculate_cost` that takes four parameters: the number of items `X`, the cost per item, the discount percentage, and the tax percentage. The function should calculate the total cost of purchasing `X` items at the given cost, applying the provided discount and tax, and ensuring the cost per item is between 1.00 and 10.00. The function should return the total cost rounded to the nearest penny. The function should have a time complexity of O(1) and a space complexity of O(1), and it should be able to handle large input values for `X`.
"""

def calculate_cost(X, cost, discount, tax):
    # Apply the discount and tax to the cost
    cost = cost * (1 - discount) * (1 + tax)
    
    # Ensure the cost per item is within the range of 1.00 to 10.00
    cost_per_item = min(max(cost, 1.00), 10.00)
    
    # Calculate the total cost
    total_cost = cost_per_item * X
    
    # Round the total cost to the nearest penny
    total_cost = round(total_cost, 2)
    
    return total_cost