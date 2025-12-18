"""
QUESTION:
Create a function called `count_frequencies` that takes a pandas DataFrame as input and returns a dictionary where keys are unique values from the DataFrame and values are their frequencies. The function should only consider rows that have more than one occurrence of the same value in different columns. The function should not take any other parameters besides the DataFrame.
"""

import pandas as pd
from collections import Counter

def count_frequencies(df):
    # Get rows with any repeated value
    repeated = df[df.duplicated(subset=None, keep=False)]

    # Count the frequency of unique values
    frequencies = Counter()
    for col in repeated:
        frequencies.update(repeated[col])

    return dict(frequencies)