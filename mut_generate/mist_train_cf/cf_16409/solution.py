"""
QUESTION:
Create a function named "custom_weighted_mean" that takes two lists, "numbers" and "weights", as input and returns the weighted mean of the numbers. The "numbers" list contains the set of numbers and the "weights" list contains their corresponding weights. The function should calculate the weighted mean by multiplying each number by its corresponding weight, summing the weighted values, and dividing by the sum of the weights.
"""

def custom_weighted_mean(numbers, weights):
    weighted_sum = sum([num * weight for num, weight in zip(numbers, weights)])
    sum_of_weights = sum(weights)
    return weighted_sum / sum_of_weights