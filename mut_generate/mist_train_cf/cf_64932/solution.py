"""
QUESTION:
Write a function named `mean_and_std_dev` that calculates the mean and standard deviation of a given list of numbers. The function should return a string containing both values if the list is not empty. If the list is empty, the function should return the message "The list is empty."
"""

import statistics

def mean_and_std_dev(lst):
    if not lst:
        return "The list is empty."
    else:
        mean_val = statistics.mean(lst)
        std_dev = statistics.stdev(lst)
        return f"Mean is {mean_val} and Standard Deviation is {std_dev}."