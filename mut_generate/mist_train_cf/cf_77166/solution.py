"""
QUESTION:
Design a function named `predictNextFibonacciElem` that takes a list of integers representing a Fibonacci series as input and returns the next element in the series. The function should handle lists with fewer than 2 elements and return `None` in such cases.
"""

def predictNextFibonacciElem(series):
    if len(series) < 2:
        return None
    return series[-1] + series[-2]