"""
QUESTION:
Write a function `total_cost` that calculates the total cost of smoothies, salads, and soups ordered by a group of friends. The function should take three parameters: `t` (number of friends who ordered smoothies at $1.99 each), `d` (number of friends who ordered salads at $3.99 each), and `p` (number of friends who ordered soups at $2.99 each), and return the total cost.
"""

def total_cost(t, d, p):
    return 1.99*t + 3.99*d + 2.99*p