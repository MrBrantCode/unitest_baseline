"""
QUESTION:
Write a function `concatenate_data_frames` that takes a list of data frames `data_frames`, an integer `start_index`, and an integer `end_index` as input parameters. The function should concatenate the data frames in the list from index `start_index` to index `end_index` (inclusive) and return the resulting concatenated data frame. The function should use the pandas library and return a new data frame without modifying the original data frames. The function should also reset the index of the resulting data frame.
"""

import pandas as pd

def concatenate_data_frames(data_frames, start_index, end_index):
    concatenated_df = pd.concat(data_frames[start_index:end_index+1], ignore_index=True)
    return concatenated_df