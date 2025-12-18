"""
QUESTION:
Given a set of coin denominations and a target amount, implement a function called `min_coins` that returns the minimum number of coins required to reach the target amount using the given denominations. The function should take two parameters: `denominations` (a list of integers representing the available coin denominations) and `target` (an integer representing the target amount). The function should return an integer representing the minimum number of coins required.
"""

def min_coins(denominations, target):
    """
    Returns the minimum number of coins required to reach the target amount using the given denominations.

    Args:
    denominations (list): A list of integers representing the available coin denominations.
    target (int): An integer representing the target amount.

    Returns:
    int: The minimum number of coins required.
    """
    # Create a list to store the minimum number of coins required for each amount from 0 to target
    min_coins_required = [float('inf')] * (target + 1)
    
    # We need 0 coins to make 0 amount
    min_coins_required[0] = 0

    # Iterate over each amount from 1 to target
    for amount in range(1, target + 1):
        # Iterate over each denomination
        for denomination in denominations:
            # If the denomination is less than or equal to the amount
            if denomination <= amount:
                # Update the minimum number of coins required for the amount
                min_coins_required[amount] = min(min_coins_required[amount], min_coins_required[amount - denomination] + 1)

    # If no combination of coins can sum up to the target amount, return -1
    if min_coins_required[target] == float('inf'):
        return -1
    else:
        return min_coins_required[target]