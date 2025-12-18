"""
QUESTION:
Implement a function `calculate_joint_angle_error(predictions, targets)` that calculates the mean squared error (MSE) between the predicted and target joint angles. The function takes two input arrays `predictions` and `targets`, both of shape (..., n_joints, 3, 3), where `n_joints` is the number of joints and the last two dimensions represent 3x3 joint angle matrices. The input arrays should be reshaped to facilitate the error calculation.
"""

import numpy as np

def calculate_joint_angle_error(predictions, targets):
    assert predictions.shape[-1] == 3 and predictions.shape[-2] == 3
    assert targets.shape[-1] == 3 and targets.shape[-2] == 3

    preds = np.reshape(predictions, [-1, 3, 3])
    targs = np.reshape(targets, [-1, 3, 3])

    error = np.mean(np.square(preds - targs))
    return error