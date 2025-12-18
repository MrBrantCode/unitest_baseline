"""
QUESTION:
Write a function `weighted_average(n1, n2, n3)` that calculates the weighted average of three integers. The weights for the three integers are 1.5, 2, and 3 respectively. The function should take three integers as input and return their weighted average.
"""

def weighted_average(n1, n2, n3):
    weight1, weight2, weight3 = 1.5, 2, 3
    return (n1 * weight1 + n2 * weight2 + n3 * weight3) / (weight1 + weight2 + weight3)