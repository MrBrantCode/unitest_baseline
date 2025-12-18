"""
QUESTION:
Write a function `calculate_average_trip_duration(df)` that takes a pandas DataFrame `df` as input, where `df` contains 'tpep_pickup_datetime' and 'tpep_dropoff_datetime' columns representing pickup and dropoff datetimes. The function should calculate the average trip duration in minutes for each day of the week and return the results as a dictionary, where keys are the days of the week and values are the average trip durations. The function should handle missing or inconsistent data.
"""

import pandas as pd

def calculate_average_trip_duration(df):
    # Convert pickup and dropoff datetimes to pandas datetime objects
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # Calculate trip durations in minutes
    df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

    # Add a new column for the day of the week
    df['day_of_week'] = df['tpep_pickup_datetime'].dt.day_name()

    # Group by day of the week and calculate the average trip duration
    average_trip_durations = df.groupby('day_of_week')['trip_duration'].mean().to_dict()

    return average_trip_durations