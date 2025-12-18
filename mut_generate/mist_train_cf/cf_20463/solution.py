"""
QUESTION:
Implement the function `weighted_median(data, weights)` that takes two lists of the same length as input: `data` - a list of positive integers, and `weights` - a list of positive integers corresponding to each number in the `data` list. The function should return the weighted median, where the sum of the weights of the numbers less than the median is equal to the sum of the weights of the numbers greater than the median. Assume the sum of all weights is odd.
"""

def weighted_median(data, weights):
    combined = sorted(zip(data, weights))
    total_weight = sum(weights)
    running_sum = 0

    for num, weight in combined:
        running_sum += weight
        if running_sum >= total_weight // 2 + 1:
            return num