"""
QUESTION:
Design a function `calculate_total_expenditure` that takes two lists as input: `Price_per_item` and `Quantity`, where the price and quantity of each item are at the corresponding index. The function should return the total expenditure by multiplying each item's price with its quantity and summing the results. The input lists are guaranteed to be of the same length.
"""

def calculate_total_expenditure(Price_per_item, Quantity):
    """
    Calculate the total expenditure by multiplying each item's price with its quantity and summing the results.
    
    Args:
        Price_per_item (list): A list of prices of each item.
        Quantity (list): A list of quantities of each item.
    
    Returns:
        int: The total expenditure.
    """
    total = 0
    for i in range(len(Price_per_item)):
        total += Price_per_item[i]*Quantity[i]
    return total