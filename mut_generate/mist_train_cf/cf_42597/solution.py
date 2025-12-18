"""
QUESTION:
Implement the `update` method in the `KalmanFilter` class to perform the following steps:
1. Predict the current state using the spacecraft's dynamics model and the state transition matrix.
2. Calculate the Kalman gain based on the predicted state, the predicted error covariance, and the sensor noise covariance.
3. Correct the predicted state using the sensor measurement and the Kalman gain.
4. Update the error covariance matrix based on the Kalman gain, the predicted error covariance, and the sensor noise covariance.

Assume the `KalmanFilter` class has the following attributes: `correctedOmega`, `measuredOmega`, `predictedOmegaError`, `stateTransitionMatrix`, `processNoiseCovariance`, and `sensorNoiseCovariance`. Use NumPy for numerical computations.
"""

import numpy as np

def kalman_update(correctedOmega, measuredOmega, predictedOmegaError, stateTransitionMatrix, processNoiseCovariance, sensorNoiseCovariance):
    """
    Perform the update step of the Kalman filter.

    Parameters:
    - correctedOmega (numpy array): The corrected state of the previous time step.
    - measuredOmega (numpy array): The sensor measurement of the current time step.
    - predictedOmegaError (numpy array): The predicted error covariance of the previous time step.
    - stateTransitionMatrix (numpy array): The state transition matrix.
    - processNoiseCovariance (numpy array): The process noise covariance matrix.
    - sensorNoiseCovariance (numpy array): The sensor noise covariance matrix.

    Returns:
    - correctedOmega (numpy array): The updated corrected state.
    - predictedOmegaError (numpy array): The updated predicted error covariance.
    """

    # Prediction step
    predictedState = np.dot(stateTransitionMatrix, correctedOmega)
    predictedErrorCovariance = np.dot(np.dot(stateTransitionMatrix, predictedOmegaError), stateTransitionMatrix.T) + processNoiseCovariance

    # Correction step
    innovation = measuredOmega - predictedState
    innovationCovariance = np.dot(np.dot(stateTransitionMatrix, predictedErrorCovariance), stateTransitionMatrix.T) + sensorNoiseCovariance
    kalmanGain = np.dot(predictedErrorCovariance, np.linalg.inv(innovationCovariance))
    correctedOmega = predictedState + np.dot(kalmanGain, innovation)
    predictedOmegaError = predictedErrorCovariance - np.dot(np.dot(kalmanGain, innovationCovariance), kalmanGain.T)

    return correctedOmega, predictedOmegaError