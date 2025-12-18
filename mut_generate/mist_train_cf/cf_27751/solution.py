"""
QUESTION:
Implement a function named `calculate_metric` that calculates and returns the average accuracy for a given metric. The function should take in four parameters: `metric`, `hits`, `misses`, `sum_precs`, and `num_examples`. If the `metric` is 'pointing', the function should calculate the average accuracy and return both the individual accuracies and the average accuracy. If the `metric` is 'average_precision', the function should calculate the class mean average precision and return it. For the 'pointing' metric, the individual accuracies are calculated as hits divided by the sum of hits and misses, and the average accuracy is the mean of the individual accuracies. Note that `sum_precs` and `num_examples` are only used for the 'average_precision' metric.
"""

import numpy as np

def calculate_metric(metric, hits, misses, sum_precs=0, num_examples=0):
    if metric == 'pointing':
        acc = hits / (hits + misses)
        avg_acc = np.mean(acc)
        return acc, avg_acc
    elif metric == 'average_precision':
        class_mean_avg_prec = sum_precs / num_examples
        return class_mean_avg_prec