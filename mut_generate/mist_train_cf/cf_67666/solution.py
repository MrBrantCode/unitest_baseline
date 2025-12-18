"""
QUESTION:
Calculate the total expenditure for a haircut and a tip. Create a function called `calculate_total_expenditure` that takes two parameters: `haircut_price` and `tip_percentage`, where `haircut_price` is the cost of the haircut and `tip_percentage` is the percentage of the tip. The function should return the total expenditure, which is the sum of the haircut price and the calculated tip. The tip is calculated by multiplying the haircut price by the tip percentage (which should be converted to a decimal by dividing by 100).
"""

def calculate_total_expenditure(haircut_price, tip_percentage):
    """
    Calculate the total expenditure for a haircut and a tip.

    Args:
        haircut_price (float): The cost of the haircut.
        tip_percentage (float): The percentage of the tip.

    Returns:
        float: The total expenditure.
    """
    # Convert the tip percentage to a decimal
    tip_percentage = tip_percentage / 100
    
    # Calculate the tip
    tip = haircut_price * tip_percentage
    
    # Calculate the total expenditure
    total_expenditure = haircut_price + tip
    
    return total_expenditure