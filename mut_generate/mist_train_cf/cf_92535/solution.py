"""
QUESTION:
Implement the function `weighted_median(data, weights)` that calculates the weighted median of a list of numbers. The function takes two lists as input: `data` - a list of numbers, and `weights` - a list of weights corresponding to each number in the data list, where the length of `data` and `weights` must be the same. The function should return the weighted median, which is the value that splits the list into two halves, where the sum of the weights of the numbers less than the median is equal to the sum of the weights of the numbers greater than the median.
"""

def weighted_median(data, weights):
    weighted_data = list(zip(data, weights))
    weighted_data.sort(key=lambda x: x[0])
    total_weight = sum(weights)
    cumulative_weight = 0
    for number, weight in weighted_data:
        cumulative_weight += weight
        if cumulative_weight >= total_weight / 2:
            return number
    return None