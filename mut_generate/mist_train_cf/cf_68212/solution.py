"""
QUESTION:
Calculate the original weights of water in two bottles given their combined weight and the weight lost by one bottle.

Create a function named `calculate_weights` that takes two parameters: `total_weight` (the combined weight of the two bottles) and `z` (the weight lost by one bottle). The function should return the original weights of the water in each bottle, with a precision of up to 0.001 kilograms.

The weight ratio between the remaining water in the first bottle (after losing `z` kilograms) and the second bottle is 2:1. The function should be able to handle a total weight up to 10^9 and a `z` up to 10^5.
"""

def calculate_weights(total_weight, z):
    left = 0
    right = total_weight
    while right-left>0.001:
        mid = (right + left)/2
        x = mid
        y = total_weight - x
        if abs(x - z - 2 * y) < 0.001:
            return round(x, 3), round(y, 3)
        elif x - z < 2 * y:
            right = mid
        else:
            left = mid
    return -1, -1  # If there is no possible solution