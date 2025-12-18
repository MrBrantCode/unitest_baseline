"""
QUESTION:
Write a function `calculate_averages(pints, propindic, variances)` that takes in a list of data points `pints`, a dictionary `propindic` where the keys are data points and the values are lists of properties, and a list of variances `variances`. The function should return a DataFrame with columns 'ProbInt' and 'FracIn' containing the average of properties for each data point, and the average of `variances`. The DataFrame should have one row per data point, with the data point in the 'ProbInt' column and its corresponding average property in the 'FracIn' column.
"""

import numpy as np
import pandas as pd

def calculate_averages(pints, propindic, variances):
    propavg = []
    for pint in pints:
        avg = np.average(propindic[pint])
        propavg.append([pint, avg])
    propavg_df = pd.DataFrame(propavg, columns=['ProbInt', 'FracIn'])
    avgvar = np.average(variances)
    propavg_df['FracIn'] = [avgvar if pd.isna(x) else x for x in propavg_df['FracIn']]
    return propavg_df