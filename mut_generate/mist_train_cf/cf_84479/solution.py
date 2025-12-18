"""
QUESTION:
Write a function named `find_median` that takes a list of numbers representing stock prices as input and returns the median value. The function should first sort the input list and then calculate the median according to whether the length of the list is odd or even.
"""

def find_median(stock_prices):
    sorted_prices = sorted(stock_prices)
    num_prices = len(sorted_prices)

    if num_prices % 2 != 0:
        median = sorted_prices[num_prices // 2]
    else:
        med1 = sorted_prices[num_prices // 2]
        med2 = sorted_prices[num_prices // 2 - 1]
        median = (med1 + med2) / 2

    return median