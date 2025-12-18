"""
QUESTION:
Given a function called `min_stamps`, write an implementation that takes two parameters: `amount` (the target aggregate monetary value) and `denominations` (a list of unique postal stamp denominations). The function should return the minimal number of stamps necessary to reach the target amount. The function must handle cases where it is impossible to form the required aggregate monetary value with the given stamp denominations.
"""

def min_stamps(amount, denominations):
    """
    Returns the minimal number of stamps necessary to reach the target amount.
    
    Args:
        amount (int): The target aggregate monetary value.
        denominations (list): A list of unique postal stamp denominations.
    
    Returns:
        int: The minimal number of stamps necessary, or -1 if impossible.
    """
    # Initialize the dynamic programming (dp) array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # No stamp is needed to reach the aggregate of $0
    
    # Loop over each denomination of stamp
    for denomination in denominations:
        # Loop from the denomination value up to the aggregate monetary value
        for i in range(denomination, amount + 1):
            # Update dp[i] to be the minimum between the current dp[i] and dp[i-denomination] + 1
            dp[i] = min(dp[i], dp[i - denomination] + 1)
    
    # Check if it is impossible to form the required aggregate monetary value
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]