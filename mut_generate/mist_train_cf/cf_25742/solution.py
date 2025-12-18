"""
QUESTION:
Write a function `generateFibonacciSeries(num)` that generates and returns the Fibonacci series up to the nth number. The function should take an integer `num` as input and return a list of integers representing the Fibonacci series. The Fibonacci series is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def entrance(num): 
    series = [0, 1] 
    for i in range(2, num): 
        series.append(series[i - 2] + series[i - 1]) 
    return series