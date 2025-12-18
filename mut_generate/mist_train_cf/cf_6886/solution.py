"""
QUESTION:
Write a function `store_and_visualize_sensor_data` that takes in sensor data as input and returns the sensor data with an additional feature to set custom thresholds for each sensor and receive notifications when sensor readings exceed or fall below the specified threshold. The function should also provide an option to export the sensor data in CSV format. The function should be optimized for performance and can handle large amounts of sensor data without any noticeable lag.
"""

import pandas as pd
import numpy as np

def store_and_visualize_sensor_data(sensor_data, threshold_settings=None, export_csv=False):
    """
    This function stores and visualizes sensor data, sets custom thresholds for each sensor, 
    and receives notifications when sensor readings exceed or fall below the specified threshold.
    
    Parameters:
    sensor_data (dict): A dictionary containing sensor data with sensor names as keys and readings as values.
    threshold_settings (dict, optional): A dictionary containing threshold settings with sensor names as keys and threshold values as values. Defaults to None.
    export_csv (bool, optional): A boolean indicating whether to export the sensor data in CSV format. Defaults to False.

    Returns:
    dict: A dictionary containing the sensor data with an additional feature to set custom thresholds for each sensor and receive notifications when sensor readings exceed or fall below the specified threshold.
    """

    # Store sensor data in a pandas DataFrame for efficient data manipulation
    df = pd.DataFrame(sensor_data)

    # Set custom thresholds for each sensor
    if threshold_settings:
        for sensor, threshold in threshold_settings.items():
            # Check if sensor readings exceed or fall below the specified threshold
            if np.any(df[sensor] > threshold['upper']) or np.any(df[sensor] < threshold['lower']):
                # Send notification when sensor reading exceeds or falls below the threshold
                print(f"Notification: {sensor} reading exceeded or fell below the threshold.")

    # Export sensor data in CSV format if required
    if export_csv:
        df.to_csv('sensor_data.csv', index=False)

    return df