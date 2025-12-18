"""
QUESTION:
You're a buyer/seller and your buisness is at stake... You ___need___ to make profit... Or at least, you need to lose the least amount of money!  
Knowing a list of prices for buy/sell operations, you need to pick two of them. Buy/sell market is evolving across time and the list represent this evolution. First, you need to buy one item, then sell it later. Find the best profit you can do.

### Example:

Given an array of prices `[3, 10, 8, 4]`, the best profit you could make would be `7` because you buy at `3` first, then sell at `10`.

# Input:

A list of prices (integers), of length 2 or more.

# Output:

The result of the best buy/sell operation, as an integer.



### Note:
Be aware you'll face lists with several thousands of elements, so think about performance.
"""

def calculate_max_profit(prices: list[int]) -> int:
    """
    Calculate the maximum profit that can be achieved by buying and selling at the optimal times.

    Parameters:
    - prices (list[int]): A list of integers representing the prices at different times.

    Returns:
    - int: The maximum profit that can be achieved.
    """
    if len(prices) < 2:
        raise ValueError("The list of prices must contain at least two elements.")
    
    min_price = prices[0]
    max_profit = float('-inf')
    
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    return max_profit