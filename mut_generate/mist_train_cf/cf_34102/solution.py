"""
QUESTION:
Create a function `generate_prediction_matrix(data, win_size)` that generates a prediction matrix from the given 3D brain activity data. The data has dimensions representing participants, features, and time points. The function should calculate the number of segments by subtracting `win_size` from the total number of time points, initialize an empty 2D array, and then concatenate the data across participants for each time window to generate the prediction matrix. The function should return the prediction matrix. The input `data` is a 3D numpy array, and `win_size` is the size of the time window for prediction.
"""

import numpy as np

def generate_prediction_matrix(data, win_size):
    n_subjs, n_features, n_TR = data.shape
    n_seg = n_TR - win_size
    train_data = np.zeros((n_features * win_size, n_seg))

    for ppt_counter in range(n_subjs):
        for window_counter in range(win_size):
            train_data[
                window_counter * n_features : (window_counter + 1) * n_features,
                :
            ] += data[ppt_counter][:, window_counter : window_counter + n_seg]

    return train_data