"""
QUESTION:
Design a function `makeChange(coinSet, value)` that implements a greedy algorithm to find the minimum number of coins required to make a given `value` using the provided `coinSet`. The function should take two parameters: `coinSet` (a list of coin denominations) and `value` (the amount to make change for). The function should return a list of coins that make up the change. If exact change is not possible, the function should throw an exception. The function should handle edge cases, such as when the entered value to change is 0.
"""

def makeChange(coinSet, value):
    """
    This function implements a greedy algorithm to find the minimum number of coins required to make a given value using the provided coinSet.
    
    Parameters:
    coinSet (list): A list of coin denominations.
    value (int): The amount to make change for.
    
    Returns:
    list: A list of coins that make up the change.
    
    Raises:
    Exception: If exact change is not possible.
    """
    
    # Sort the coin set in descending order
    coinSet.sort(reverse=True)
    
    # Initialize variables to store the result
    resultCoins = []
    remainingValue = value
    
    # Iterate over the coin set
    for coin in coinSet:
        # While the coin value is not more than the remaining value
        while coin <= remainingValue:
            # Subtract the coin value from the remaining value
            remainingValue -= coin
            # Add the coin to the result
            resultCoins.append(coin)
    
    # If exact change is not possible, raise an exception
    if remainingValue != 0:
        raise Exception("Exact Change Not Possible")
    
    return resultCoins