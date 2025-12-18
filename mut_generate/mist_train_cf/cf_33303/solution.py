"""
QUESTION:
Write a function `summarize` that takes two parameters: `vars` (a list of variable names) and `df` (a pandas DataFrame). The function should calculate and return a summary table for the variables in `vars` with the following statistics: Count, Mean, Standard Deviation, Minimum, 25th Percentile, Median, 75th Percentile, and Maximum. The summary table should have the variables as rows and the statistics as columns.
"""

import pandas as pd

def summarize(vars, df):
    summary_stats = df[vars].describe().T
    summary_stats = summary_stats[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
    summary_stats.columns = ['Count', 'Mean', 'Standard Deviation', 'Minimum', '25th Percentile', 'Median', '75th Percentile', 'Maximum']
    return summary_stats