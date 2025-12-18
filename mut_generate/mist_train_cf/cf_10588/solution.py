"""
QUESTION:
Write a function `calculate_stock_span` that takes an array of daily stock prices as input and returns an array of span values. The span value at each index `i` is the maximum number of consecutive days just before the given day `i`, for which the price of the stock on the current day is less than or equal to its price on the given day.
"""

def calculate_stock_span(prices):
    """
    Calculate the stock span for a given list of daily stock prices.

    The span value at each index `i` is the maximum number of consecutive days just 
    before the given day `i`, for which the price of the stock on the current day is 
    less than or equal to its price on the given day.

    Args:
        prices (list): A list of daily stock prices.

    Returns:
        list: A list of span values.
    """
    stack = []
    span = [0] * len(prices)

    stack.append(0)
    span[0] = 1

    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    return span