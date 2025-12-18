"""
QUESTION:
Implement the function `calculate_individual_r_squared(scores)` that takes a list of scores as input and returns a list of individual coefficients of determination for each pair of consecutive scores. The individual coefficient of determination for a pair of scores (x, y) is calculated as (1 - (residual sum of squares / total sum of squares)), where the residual sum of squares is the sum of squared differences between the actual y-values and the predicted y-values, and the total sum of squares is the sum of squared differences between the actual y-values and the mean of y-values.
"""

def calculate_individual_r_squared(scores):
    individual_r_squared = []
    for i in range(len(scores) - 1):
        x = scores[i]
        y = scores[i + 1]
        mean_y = sum(scores) / len(scores)
        total_sum_squares = sum([(val - mean_y) ** 2 for val in scores])
        predicted_y = x
        residual_sum_squares = (y - predicted_y) ** 2
        individual_r_squared.append(1 - (residual_sum_squares / total_sum_squares))
    return individual_r_squared