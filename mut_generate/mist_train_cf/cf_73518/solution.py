"""
QUESTION:
Given a list of numbers, create a function named `compute_running_mean` that calculates the running mean (or cumulative average) of the list, where the mean at each index is the average of all numbers up to that index. The function should return a list of these running means. Assume that the input list will contain only numbers.
"""

def compute_running_mean(data):
    running_mean = []
    cum_sum = 0.0
    for i, x in enumerate(data, 1):
        cum_sum += x
        running_mean.append(cum_sum / i)
    return running_mean