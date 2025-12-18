"""
QUESTION:
Write a function `compare_dataframes` that compares two pandas DataFrames `expected` and `actual` with options to ignore schema metadata and comments. The function takes four parameters: `expected`, `actual`, `ignore_schema_metadata`, and `ignore_comments`. If `expected` is None, the function asserts that `actual` is also None and returns True. If `ignore_schema_metadata` is True, it ignores differences in index order. If `ignore_comments` is True, it ignores object columns. The function returns True if the DataFrames are equal based on the specified criteria and False otherwise.
"""

import pandas as pd

def compare_dataframes(expected, actual, ignore_schema_metadata=False, ignore_comments=False):
    if expected is None:
        assert actual is None, 'The expected DataFrame is None, but the actual DataFrame is not.'
        return True  

    if ignore_schema_metadata:
        expected = expected.reset_index(drop=True, inplace=False)
        actual = actual.reset_index(drop=True, inplace=False)

    if ignore_comments:
        expected = expected.select_dtypes(exclude=['object'])
        actual = actual.select_dtypes(exclude=['object'])

    return expected.equals(actual)