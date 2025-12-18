"""
QUESTION:
Complete the `process_stimuli_data` function to process a DataFrame `df` with the following requirements:
- Extract the category and name of the stimuli from the 'stim_file' column and populate the 'stim_category' and 'stim_name' columns, respectively. The 'stim_file' column contains file names in the format "category_imageName.bmp".
- Update the 'recognition_performance' column based on the actual and perceived novelty of the stimuli. If the stimuli are perceived as novel, set the 'recognition_performance' to 'novel', otherwise set it to 'familiar'. The perceived novelty information is available in a column named 'perceived_novelty'.

The DataFrame `df` has columns 'trial_number', 'stim_file', 'stim_category', 'stim_name', and 'recognition_performance', and 'perceived_novelty'.
"""

import re

def process_stimuli_data(df):
    """
    Process a DataFrame to extract the category and name of the stimuli from the 'stim_file' column 
    and update the 'recognition_performance' column based on the actual and perceived novelty of the stimuli.

    Args:
    df (DataFrame): DataFrame containing columns 'trial_number', 'stim_file', 'stim_category', 'stim_name', 
                    'recognition_performance', and 'perceived_novelty'.

    Returns:
    DataFrame: Processed DataFrame with 'stim_category', 'stim_name', and 'recognition_performance' updated.
    """
    # Extract category and name of the stimuli from 'stim_file' and populate 'stim_category' and 'stim_name' columns
    df['stim_category'] = df['stim_file'].apply(lambda x: re.findall('(.+?)_', x)[0])
    df['stim_name'] = df['stim_file'].apply(lambda x: re.findall('_(.+?)[.]', x)[0])

    # Update 'recognition_performance' column based on actual and perceived novelty
    df['recognition_performance'] = df['perceived_novelty'].apply(lambda x: 'novel' if x == 'novel' else 'familiar')

    return df