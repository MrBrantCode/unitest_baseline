"""
QUESTION:
Write a function named `median_and_standard_deviation` that takes a list of numbers as input and returns a tuple containing the median and standard deviation of the list. The function should not sort the input list. If the list has an even number of elements, the median should be calculated as the average of the number of even and odd elements. If the list has an odd number of elements, the median can be approximated as the average of the list.
"""

import math

def median_and_standard_deviation(l: list):
    # find even and odd elements,
    even = sum(1 for elem in l if elem % 2 == 0)
    odd = len(l) - even

    # compute the sum and squared sum of the elements
    total_sum = sum(l)
    squared_sum = sum(e ** 2 for e in l)

    # compute the average and standard deviation
    average = total_sum / len(l)
    standard_deviation = math.sqrt(squared_sum/len(l) - average**2)

    if len(l) % 2 == 0:  # even length
        median = (even + odd) / 2
    else:  # odd length
        median = average

    return median, standard_deviation