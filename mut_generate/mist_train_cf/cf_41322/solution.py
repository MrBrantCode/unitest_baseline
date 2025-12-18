"""
QUESTION:
Implement the `evaluate_function` function, which takes a 2D numpy array `eval_points` with shape `(number_eval_points, dim_domain)` and returns a 3D numpy array with shape `(n_samples, number_eval_points, dim_codomain)` representing the results of evaluating a mathematical function at each point in `eval_points` for `n_samples` samples.
"""

import numpy as np

def evaluate_function(eval_points: np.ndarray) -> np.ndarray:
    """
    Evaluate a mathematical function at specified points.

    Args:
        eval_points (numpy.ndarray): Numpy array with shape
            ``(number_eval_points, dim_domain)`` with the
            evaluation points.

    Returns:
        (numpy.ndarray): Numpy 3d array with shape
            ``(n_samples, number_eval_points, dim_codomain)`` with the
            result of the evaluation. The entry ``(i,j,k)`` will contain
            the value k-th image dimension of the i-th sample, at the
            j-th evaluation point.
    """
    n_samples = 2  
    dim_codomain = 3  
    n_eval_points, dim_domain = eval_points.shape

    result = np.zeros((n_samples, n_eval_points, dim_codomain))

    for i in range(n_samples):
        for j in range(n_eval_points):
            x, y = eval_points[j]  
            result[i, j] = [x, x + y, x * y]  

    return result