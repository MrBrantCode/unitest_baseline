"""
QUESTION:
Write a function `calculateSpan(prices)` to solve the Stock Span problem. The function takes an array of daily stock prices as input and returns an array of span values for each day. The span value for a given day is the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day. The function should have a time complexity of O(n) and should not use any additional data structures. The input array will have at most 10^5 elements, and each element in the array will be an integer between 1 and 10^5.
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