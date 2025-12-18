"""
QUESTION:
Implement a function `detect_anomalies(logs)` that takes a list of log dictionaries as input. Each log dictionary contains 'temperature' and 'pressure' keys, representing an integer temperature and a floating-point pressure, respectively. Identify any anomalies in the data where the temperature is outside the range of 35 to 38 degrees Celsius or the pressure is outside the range of 2.5 to 3.5. The function should return a list of indices (0-based) where anomalies are detected.
"""

def detect_anomalies(logs):
    """
    Identify anomalies in temperature and pressure logs.

    Args:
        logs (list): A list of log dictionaries with 'temperature' and 'pressure' keys.

    Returns:
        list: A list of indices where anomalies are detected.
    """
    anomalies = []
    for i, log in enumerate(logs):
        if log['temperature'] < 35 or log['temperature'] > 38 or log['pressure'] < 2.5 or log['pressure'] > 3.5:
            anomalies.append(i)
    return anomalies