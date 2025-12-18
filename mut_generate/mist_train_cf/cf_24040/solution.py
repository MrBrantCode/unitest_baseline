"""
QUESTION:
Write a function `stock_span` that takes an array of stock prices as input and returns an array where the value at each index represents the number of days the stock's price was less than or equal to the price at that index, looking from left to right. The function should use a stack to keep track of the indices of the prices. If a price is greater than all previous prices, the value at that index should be the index plus one. The function should return the array of stock spans.
"""

def stock_span(arr):
    stack = []
    stock_span = [0] * len(arr)
    stack.append(0)
    stock_span[0] = 1

    for i in range(1, len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if not stack:
            stock_span[i] = i + 1
        else:
            stock_span[i] = i - stack[-1]
        stack.append(i)

    return stock_span