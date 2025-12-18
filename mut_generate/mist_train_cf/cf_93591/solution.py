"""
QUESTION:
Create a function called `calculate_weighted_average` that calculates the weighted average score of a list of numbers. The function should take two parameters: a list of numbers and a list of corresponding weights. The function should return the weighted average score as a float. If the lists are empty or all weights are zero or negative, the function should return 0.
"""

def calculate_weighted_average(numbers, weights):
    if len(numbers) == 0 or len(weights) == 0:
        return 0

    total = 0
    total_weights = 0

    for i in range(len(numbers)):
        if weights[i] <= 0:
            continue

        total += numbers[i] * weights[i]
        total_weights += weights[i]

    if total_weights == 0:
        return 0

    return total / total_weights