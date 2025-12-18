"""
QUESTION:
Create a function called calculate_psi that calculates the Population Stability Index (PSI) for comparing the distribution of a variable between a reference data set and a current data set. The function should be able to handle both continuous and categorical data. For continuous data, the number of bins should be a variable input, defaulting to 10. For categorical data with less than 10 possible values, the function should compare the distributions directly without binning.
"""

import numpy as np
import pandas as pd

def calculate_psi(reference, current, bins=10, categorical=False):
    """
    Calculate the Population Stability Index (PSI) between a reference data set and a current data set.

    Parameters:
    - reference (array-like): Reference data set.
    - current (array-like): Current data set.
    - bins (int): Number of bins for continuous data. Defaults to 10.
    - categorical (bool): Whether the data is categorical. Defaults to False.

    Returns:
    - float: Population Stability Index (PSI).
    """

    # Check if data is categorical and has less than 10 possible values
    if categorical and len(set(reference)) < 10:
        reference_counts = pd.Series(reference).value_counts()
        current_counts = pd.Series(current).value_counts()
        all_values = set(list(reference_counts.index) + list(current_counts.index))
        psi = 0
        for value in all_values:
            reference_percent = reference_counts.get(value, 0) / len(reference)
            current_percent = current_counts.get(value, 0) / len(current)
            psi += (reference_percent - current_percent) * np.log(reference_percent / current_percent)
        return psi

    # Binning for continuous data
    reference_binned, bin_edges = np.histogram(reference, bins=bins)
    current_binned, _ = np.histogram(current, bins=bin_edges)

    # Calculate PSI
    reference_percent = reference_binned / len(reference)
    current_percent = current_binned / len(current)
    psi = 0
    for i in range(len(reference_binned)):
        if reference_percent[i] > 0 and current_percent[i] > 0:
            psi += (reference_percent[i] - current_percent[i]) * np.log(reference_percent[i] / current_percent[i])
    return psi