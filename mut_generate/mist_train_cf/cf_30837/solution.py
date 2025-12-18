"""
QUESTION:
Given a set of sensor data with sensor IDs, timestamps, and sensor readings, write a function `find_anomalies` that identifies sensor readings that deviate from the average reading by more than a given threshold. The function should return a list of tuples, where each tuple contains the timestamp and sensor ID of an anomaly. The sensor readings are floating-point numbers, the timestamps are datetime objects, and the sensor IDs are integers. The function should take the sensor data, a list of sensor readings, a list of timestamps, a list of sensor IDs, and a threshold value as inputs.
"""

import numpy as np

def find_anomalies(sensor_data, timestamps, sensor_ids, threshold):
    """
    Identify sensor readings that deviate from the average reading by more than a given threshold.

    Args:
    - sensor_data (list): A list of sensor readings.
    - timestamps (list): A list of timestamps corresponding to the sensor readings.
    - sensor_ids (list): A list of sensor IDs corresponding to the sensor readings.
    - threshold (float): The threshold value for anomaly detection.

    Returns:
    - list: A list of tuples, where each tuple contains the timestamp and sensor ID of an anomaly.
    """
    # Calculate the average sensor reading
    average_reading = np.mean(sensor_data)

    # Identify anomalies and store their timestamps and sensor IDs
    anomalies = []
    for i in range(len(sensor_data)):
        if abs(sensor_data[i] - average_reading) > threshold:
            anomalies.append((timestamps[i], sensor_ids[i]))

    return anomalies