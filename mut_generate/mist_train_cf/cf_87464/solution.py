"""
QUESTION:
Write a function calculateSpan that takes a list of integers representing daily stock prices as input and returns a list of integers representing the span of the stock's price for each day. The span of the stock's price on a given day is the maximum number of consecutive days just before the given day for which the price of the stock on the current day is less than or equal to its price on the given day. The input list will have at most 10^5 elements, and each element will be an integer between 1 and 10^5. The function should have a time complexity of O(n), where n is the number of days.
"""

def calculateSpan(prices):
    n = len(prices)
    span = [1] * n
    lastIndex = 0

    for i in range(1, n):
        while lastIndex > 0 and prices[i] >= prices[lastIndex]:
            lastIndex -= 1
        
        if lastIndex == 0:
            span[i] = i + 1
        else:
            span[i] = i - lastIndex
        
        lastIndex = i

    return span