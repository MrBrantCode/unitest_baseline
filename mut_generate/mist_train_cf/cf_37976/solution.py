"""
QUESTION:
Write a function `weighted_variance_average(data)` that takes a dataset `data` with metadata and experimental data, where the metadata is a list of strings and the experimental data is a list of numerical values, and returns the weighted average of the variances of the experimental data grouped by the metadata. If a group contains only one data point, it is not considered for variance calculation. If no variances are calculated, the function should return the mean of the error data. The dataset `data` has the following attributes: `metadata`, `exp`, and `err`, representing the metadata, experimental data, and error data, respectively.
"""

import numpy as np

def weighted_variance_average(data):
    groups = {}
    for x, y in zip(data.metadata, data.exp):
        if x not in groups:
            groups[x] = []
        groups[x].append(y)
    
    variances, weights = [], []
    for group in groups.values():
        group_size = len(group)
        if group_size > 1:
            variances.append(np.var(group, ddof=1))
            weights.append(group_size - 1)
    
    if not variances:
        return np.mean(data.err)
    
    return float(np.average(variances, weights=weights))