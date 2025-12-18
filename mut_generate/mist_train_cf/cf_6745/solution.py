"""
QUESTION:
Write a function `calculate_cost(X, cost, discount_percentage, tax_percentage)` to calculate the cost of purchasing X items at a given cost, applying a discount and tax, and rounding the final cost to the nearest penny. The function should handle large input values for X and have a time complexity of O(1) and a space complexity of O(1). The input values for X must be positive integers and cost in the range of 0.01 to 100.00, while the discount and tax percentages should be in the range of 0.00 to 0.50 and 0.00 to 1.00, respectively.
"""

def entrance(X, cost, discount_percentage, tax_percentage):
    # Calculate the total cost before applying discounts or taxes
    total_cost = X * cost
    
    # Apply the discount
    discount_amount = total_cost * discount_percentage
    total_cost -= discount_amount
    
    # Apply the tax
    tax_amount = total_cost * tax_percentage
    total_cost += tax_amount
    
    # Round the final cost to the nearest penny
    rounded_cost = round(total_cost, 2)
    
    return rounded_cost