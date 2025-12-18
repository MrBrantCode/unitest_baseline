"""
QUESTION:
Implement a function `mean(numbers, weights=None)` that calculates the mean of a list of numbers, considering the following requirements:

- The function should handle edge cases such as an empty list or a list with extremely large numbers.
- If a list of weights is provided, the function should calculate the weighted mean.
- The function should preserve decimal precision in the returned value.
- If the input list is empty or the list of numbers and weights have different lengths, the function should return None.
"""

def calculate_mean(numbers, weights=None):
    if not numbers: 
        return None

    total_value = 0
    total_weight = 0
    
    if weights:
        if len(numbers) != len(weights):
            return None

        for num, weight in zip(numbers, weights):
            total_value += num * weight
            total_weight += weight
        mean_value = total_value / total_weight
    
    else:
        mean_value = sum(numbers) / len(numbers)

    return mean_value