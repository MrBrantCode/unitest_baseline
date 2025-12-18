"""
QUESTION:
Given a dataset, determine a suitable value for k in the K-Nearest Neighbors (KNN) algorithm. The total number of data points in the dataset should be used to calculate a starting value for k.
"""

def k_value(data_points):
    """
    Calculate a suitable starting value for k in the K-Nearest Neighbors (KNN) algorithm.
    
    The total number of data points in the dataset is used to calculate a starting value for k.
    
    Parameters:
    data_points (int): The total number of data points or observations in the dataset.
    
    Returns:
    int: A suitable starting value for k.
    """
    import math
    k = round(math.sqrt(data_points))
    return k