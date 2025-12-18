"""
QUESTION:
Write a function `total_cost` that calculates the total cost of running four restaurants for a specified number of days. The first restaurant has an initial investment cost `I` and daily operational and labor costs `C`. The other three restaurants have an initial investment cost of ¾ of `I` each and the same daily operational and labor costs `C`. The function should take two parameters: `D` (the number of days), `I` (the initial investment for one restaurant), and `C` (the daily operational and labor cost for one restaurant).
"""

def total_cost(D, I, C):
    return 3.25 * I + 4 * C * D