"""
QUESTION:
Create a function `standardize_metrics` that takes a dictionary of student metrics, where each key is a metric name and each value is a list of corresponding metric values. The function should standardize each metric to the same range or scale using either Z-score standardization or Min-Max normalization, and then combine the standardized metrics based on their given weightages. The function should return a list of standardized values, one for each student. The weightages are: % of assignments completed (10%), % feedback received from teachers (10%), number of assignments completed (10%), average attendance in days (10%), quality of projects submitted (40%), and projects (20%).
"""

import numpy as np

def standardize_metrics(metrics):
    """
    Standardize student metrics using Z-score standardization and combine them based on their given weightages.

    Args:
        metrics (dict): A dictionary of student metrics where each key is a metric name and each value is a list of corresponding metric values.

    Returns:
        list: A list of standardized values, one for each student.
    """
    # Define the weightages for each metric
    weightages = {
        '% of assignments completed': 0.1,
        '% feedback received from teachers': 0.1,
        'number of assignments completed': 0.1,
        'average attendance in days': 0.1,
        'quality of projects submitted': 0.4,
        'projects': 0.2
    }

    # Initialize a list to store the standardized values
    standardized_values = []

    # Iterate over each student's metrics
    for student_metrics in zip(*metrics.values()):
        # Initialize the standardized value for the current student to 0
        standardized_value = 0

        # Iterate over each metric and its weightage
        for metric, weightage in weightages.items():
            # Get the current metric value for the student
            metric_value = student_metrics[list(metrics.keys()).index(metric)]

            # Calculate the mean and standard deviation of the metric values
            mean = np.mean(metrics[metric])
            std_dev = np.std(metrics[metric])

            # Standardize the metric value using Z-score standardization
            standardized_metric_value = (metric_value - mean) / std_dev

            # Add the weighted standardized metric value to the standardized value
            standardized_value += weightage * standardized_metric_value

        # Append the standardized value to the list of standardized values
        standardized_values.append(standardized_value)

    return standardized_values