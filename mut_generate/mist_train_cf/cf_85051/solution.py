"""
QUESTION:
Given a set of distinct postage stamp denominations and a specific total postal value, write a function `min_stamps` that returns the least number of stamps required to reach the total postal value. The function should take two parameters: a list of integers representing the stamp denominations and an integer representing the total postal value.
"""

def min_stamps(stamps, total):
    """
    Returns the least number of stamps required to reach the total postal value.

    Args:
    stamps (list): A list of integers representing the stamp denominations.
    total (int): An integer representing the total postal value.

    Returns:
    int: The least number of stamps required to reach the total postal value.
    """
    
    # Create a list to store the minimum number of stamps for each postal value
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 stamps are required to reach a total postal value of 0
    dp[0] = 0
    
    # Iterate over each postal value from 1 to the total
    for i in range(1, total + 1):
        # Iterate over each stamp denomination
        for stamp in stamps:
            # If the stamp denomination is not greater than the current postal value
            if stamp <= i:
                # Update the minimum number of stamps required for the current postal value
                dp[i] = min(dp[i], dp[i - stamp] + 1)
    
    # Return the minimum number of stamps required to reach the total postal value
    return dp[total] if dp[total] != float('inf') else -1