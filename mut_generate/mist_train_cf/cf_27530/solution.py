"""
QUESTION:
Implement the `calculate_entropy(data)` function to calculate the entropy of a given data set. The function should take a list of integers `data` as input and return the entropy value calculated based on the frequency of each unique integer in the data set. The entropy (H) of a data set is calculated using the formula: 
\[ H = - \sum_{i=1}^{n} P(x_i) \cdot \log_2(P(x_i)) \]
where:
- \( n \) is the total number of unique integers in the data set.
- \( P(x_i) \) is the probability of occurrence of the \( i^{th} \) unique integer in the data set.

The function should not take any other arguments other than the input data set.
"""

import math

def calculate_entropy(data):
    unique_values = list(set(data))
    total_count = len(data)
    entropy = 0

    for value in unique_values:
        probability = data.count(value) / total_count
        entropy -= probability * math.log2(probability)

    return entropy