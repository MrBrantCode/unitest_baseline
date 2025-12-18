"""
QUESTION:
Write a function `minCoins(amount: int, coins: List[int]) -> int` to find the minimum number of coins required to make the given amount using a list of available coin denominations. The function should return -1 if it is not possible to make the given amount using the available coin denominations.

The given `amount` is a positive integer and the list `coins` is sorted in ascending order and contains distinct positive integers.
"""

def minCoins(amount: int, coins: list[int]) -> int:
    """
    This function calculates the minimum number of coins required to make a given amount
    using a list of available coin denominations.

    Args:
        amount (int): The target amount to make.
        coins (list[int]): A list of available coin denominations.

    Returns:
        int: The minimum number of coins required to make the given amount. Returns -1 if it's not possible.
    """

    # Create a table to store the minimum number of coins required for each amount
    dp = [float('inf')] * (amount + 1)
    
    # It takes 0 coins to make an amount of 0
    dp[0] = 0
    
    # Iterate through all amounts from 1 to the given amount
    for i in range(1, amount + 1):
        # Iterate through all available coin denominations
        for coin in coins:
            # Check if we can use the coin to make the current amount
            if i >= coin:
                # Update the value of dp[i] to be the minimum between its current value and dp[i - coin] + 1
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If the value of dp[amount] is still a large number, it means that it's not possible to make the given amount
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]