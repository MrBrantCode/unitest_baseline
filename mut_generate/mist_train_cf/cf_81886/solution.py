"""
QUESTION:
Write a function `calculate_seats_info` that takes a pandas DataFrame with columns 'job' and 'seats' as input. The function should return a dictionary with the maximum value, minimum value, mode, median, and the job with the most seats in the 'seats' column. If there are multiple jobs with the same maximum number of seats, the function should return the first job encountered.
"""

import pandas as pd

def calculate_seats_info(df):
    """
    Calculate the maximum value, minimum value, mode, median, and the job with the most seats in the 'seats' column.

    Args:
        df (pd.DataFrame): A pandas DataFrame with columns 'job' and 'seats'.

    Returns:
        dict: A dictionary with the maximum value, minimum value, mode, median, and the job with the most seats.
    """
    
    # Calculate maximum value
    max_val = df['seats'].max()
    
    # Calculate minimum value
    min_val = df['seats'].min()
    
    # Calculate mode
    mode_val = df['seats'].mode()[0]
    
    # Calculate median
    median_val = df['seats'].median()
    
    # Calculate the job with the most seats
    most_seats = df[df.seats == df.seats.max()]['job'].values[0]
    
    # Return the calculated values as a dictionary
    return {
        'max': max_val,
        'min': min_val,
        'mode': mode_val,
        'median': median_val,
        'job_with_most_seats': most_seats
    }