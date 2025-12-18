"""
QUESTION:
Write a function `sum_of_fourth_power_of_odds(n)` to find the sum of the fourth power of the first n odd natural numbers. The function should be implemented using recursion, without using any built-in Python functions or libraries, and with a time complexity of O(n).
"""

def sum_of_fourth_power_of_odds(n):
    if n == 1:
        return 1
    else:
        return ((2*n-1)**4 + sum_of_fourth_power_of_odds(n-1))