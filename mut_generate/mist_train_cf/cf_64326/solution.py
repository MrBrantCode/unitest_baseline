"""
QUESTION:
Given an integer `d` between 0 and 9, and two positive integers `low` and `high` as lower and upper bounds, respectively, where `0 <= d <= 9` and `1 <= low <= high <= 2*10^8`, write a function `sum_of_digit(d, low, high)` that returns the sum of all integers between `low` and `high`, including the bounds `low` and `high`, where `d` occurs as a digit.
"""

def sum_of_digit(d, low, high):
    return sum(i for i in range(low, high+1) if str(d) in str(i))