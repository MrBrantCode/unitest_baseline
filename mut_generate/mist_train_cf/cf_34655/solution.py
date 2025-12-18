"""
QUESTION:
Write a function `calculate_entropy(dataset)` that takes a list of values `dataset` as input, calculates the entropy of the dataset using the formula \( H(X) = -\sum_{i=1}^{n} P(x_i) \cdot \log_2(P(x_i)) \), where \( P(x_i) \) is the probability of occurrence of the i-th distinct value in the dataset, and returns the result rounded to 2 decimal places.
"""

import math

def calculate_entropy(dataset):
    total_count = len(dataset)
    value_counts = {}
    
    # Count the occurrences of each distinct value in the dataset
    for value in dataset:
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    
    entropy = 0
    for count in value_counts.values():
        probability = count / total_count
        entropy -= probability * math.log2(probability)
    
    return round(entropy, 2)