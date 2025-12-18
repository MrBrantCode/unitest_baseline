"""
QUESTION:
Create a function `transform_list` that takes a list of numerical values as input and returns a structured numpy array with three fields: 'value', 'cumulative_sum', and 'moving_average'. The 'cumulative_sum' field should contain the cumulative sum of the elements, and the 'moving_average' field should contain the moving average of the last three elements at each stage, handling the start of the array where fewer than three elements have been processed.
"""

import numpy as np

def transform_list(input_list):
   
    # Create structured numpy array
    dtype = [('value', int), ('cumulative_sum', int), ('moving_average', float)]
    output_array = np.zeros(len(input_list), dtype=dtype)

    # Calculate cumulative sum and moving average
    for i, val in enumerate(input_list):
        output_array[i]['value'] = val
        output_array[i]['cumulative_sum'] = sum(input_list[:i+1])
        if i < 3: # handle start of array where less than 3 elements are present
            output_array[i]['moving_average'] = np.mean(input_list[:i+1])
        else:
            output_array[i]['moving_average'] = np.mean(input_list[i-2:i+1])

    return output_array