"""
QUESTION:
Write a function named `filter_out_nulls_and_calculate` that takes two lists of numbers, removes any `None` values, calculates the coefficient of variation for each list, and calculates the correlation coefficient between the two lists. The function should handle the case where either list is empty after removing `None` values, and should also handle the case where the lists have different lengths after removing `None` values.
"""

import math
import statistics
import numpy

def filter_out_nulls_and_calculate(list1, list2):
    #Filter out null values
    list1 = list(filter(None, list1))
    list2 = list(filter(None, list2))

    #Handle divide by zero scenarios
    if len(list1)==0 or len(list2)==0:
        return "Cannot calculate with empty or all null values list"

    #calculate coefficient of variation (standard deviation divided by mean)
    cov1 = statistics.stdev(list1) / statistics.mean(list1)
    cov2 = statistics.stdev(list2) / statistics.mean(list2)
    print("Coefficient of Variation for list1: ", cov1)
    print("Coefficient of Variation for list2: ", cov2)

    #calculate correlation coefficient
    try:
        cor = numpy.corrcoef(list1, list2)[0][1]
        print("Correlation Coefficient: ", cor)
    except:
        print("Cannot compute correlation coefficient. Different number of elements in the lists or other errors")