"""
QUESTION:
Calculate the maximum potential loss of a calendar spread, which is the difference between the cost of the longer-dated option (Premium Paid) and the proceeds from the short-dated option (Premium Received). Assume the position is closed when the short expiry occurs.
"""

def calendar_spread_max_loss(premium_paid, premium_received):
    """
    Calculate the maximum potential loss of a calendar spread.
    
    Parameters:
    premium_paid (float): The cost of the longer-dated option.
    premium_received (float): The proceeds from the short-dated option.
    
    Returns:
    float: The maximum potential loss.
    """
    return premium_paid - premium_received