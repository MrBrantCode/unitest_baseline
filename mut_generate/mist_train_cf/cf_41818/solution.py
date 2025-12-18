"""
QUESTION:
Implement the function `calculate_left_cosine(left_pred_conf, left_pred_orientation)` that takes two NumPy arrays `left_pred_conf` and `left_pred_orientation` as input and returns the `left_cos` array. The function should first find the indices of the maximum values along the columns of `left_pred_conf` using `np.argmax`, then extract the corresponding elements from `left_pred_orientation` using advanced indexing, and finally return the first column of the extracted elements as the `left_cos` array. The input arrays `left_pred_conf` and `left_pred_orientation` have shapes (n, m) and (m, 2) respectively, where n and m are integers.
"""

import numpy as np

def calculate_left_cosine(left_pred_conf, left_pred_orientation):
    left_argmax = np.argmax(left_pred_conf, axis=1)
    left_orient = left_pred_orientation[left_argmax, :]
    left_cos = left_orient[:, 0]
    return left_cos