"""
QUESTION:
Define a function `find_frequency_and_remove_outliers` that takes a list of integers as input and returns a dictionary where the keys are the integers from the input list and the values are their frequencies. The function should also remove any outlier values from the frequency distribution using the Z-score method, where an outlier is defined as any data point more than 1.5 interquartile ranges (IQRs) below the first quartile or above the third quartile. The input list should contain at least four different elements, and the standard deviation of the frequencies should not be zero.
"""

import numpy as np

def find_frequency_and_remove_outliers(my_list):
    freq_dict = {}
    for i in my_list:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    # Calculate the Z-scores
    z_scores = [(x - np.mean(list(freq_dict.values()))) / np.std(list(freq_dict.values())) for x in list(freq_dict.values())]

    # Remove outliers: data points more than 1.5 IQRs below Q1 or above Q3
    Q1 = np.percentile(z_scores, 25)
    Q3 = np.percentile(z_scores, 75)
    IQR = Q3 - Q1
    outlier_indexes = [i for i, x in enumerate(z_scores) if x < (Q1 - 1.5*IQR) or x > (Q3 + 1.5*IQR)]
    # Get the corresponding keys for the outliers
    outlier_keys = [list(freq_dict.keys())[i] for i in outlier_indexes]
    # Remove the outliers from the frequency dictionary
    for k in outlier_keys:
        del freq_dict[k]
    
    return freq_dict