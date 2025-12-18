"""
QUESTION:
Write a function `calculateSpan(prices)` that takes an array of integers representing daily stock prices and returns an array of integers representing the span of the stock's price for each day. The span of the stock's price on a given day is the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day. The input array will have at most 10^5 elements, and each element will be an integer between 1 and 10^5.
"""

def calculateSpan(prices):
    """
    Calculate the span of the stock's price for each day.

    Args:
    prices (list): A list of integers representing daily stock prices.

    Returns:
    list: A list of integers representing the span of the stock's price for each day.
    """
    stack = []
    spans = [0] * len(prices)

    stack.append(0)
    spans[0] = 1

    for i in range(1, len(prices)):
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()

        if not stack:
            spans[i] = i + 1
        else:
            spans[i] = i - stack[-1]

        stack.append(i)

    return spans