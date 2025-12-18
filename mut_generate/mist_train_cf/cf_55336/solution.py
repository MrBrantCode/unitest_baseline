"""
QUESTION:
Write a Python function `filter_high_risk_data` that takes in a dataset, represented as a list of dictionaries where each dictionary contains a 'risk_factor' key with a float value, and a threshold value. The function should return a list of dictionaries from the dataset where the 'risk_factor' value exceeds the given threshold.
"""

def filter_high_risk_data(dataset, threshold):
    """
    Filter a dataset to include only the data points where the 'risk_factor' value exceeds the given threshold.

    Args:
        dataset (list): A list of dictionaries where each dictionary contains a 'risk_factor' key with a float value.
        threshold (float): The threshold value for the 'risk_factor'.

    Returns:
        list: A list of dictionaries from the dataset where the 'risk_factor' value exceeds the given threshold.
    """
    return [data for data in dataset if data['risk_factor'] > threshold]