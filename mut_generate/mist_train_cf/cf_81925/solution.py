"""
QUESTION:
Write a function `detect_waves` that takes a time series dataset as input and returns the number of "waves" in the dataset. A "wave" is a local maximum in the dataset, where the preceding and following points are lower. Implement this function using one or more of the following approaches: local maxima/minima, convolutional filters, wavelet transform, Fourier transform, machine learning models, transfer entropy, change point detection, or AutoRegressive Integrated Moving Average (ARIMA). The function should work with a variety of input datasets and may require tuning and preprocessing to accurately identify "waves."
"""

def detect_waves(dataset):
    """
    Detect the number of "waves" in a time series dataset.
    
    A "wave" is a local maximum in the dataset, where the preceding and following points are lower.
    
    Parameters:
    dataset (list): A list of numbers representing the time series dataset.
    
    Returns:
    int: The number of "waves" in the dataset.
    """
    waves = 0
    for i in range(1, len(dataset) - 1):
        if dataset[i] > dataset[i - 1] and dataset[i] > dataset[i + 1]:
            waves += 1
    return waves