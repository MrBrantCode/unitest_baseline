"""
QUESTION:
Implement the `acceptance_probability` method in the `SimulatedAnnealingOptimizer` class. The method should calculate the acceptance probability for a potential solution based on the current and potential scores and temperatures. The formula for the acceptance probability is given by `e^(score_diff_norm * temp)`, where `score_diff_norm` is the normalized score difference between the current and potential solutions, and `temp` is the temperature difference between the current and potential solutions. The `score_diff_norm` should be calculated as `(_p1_.score_current - _p2_.score_current) / denom`, and `temp` should be calculated as `(1 / _p1_.temp) - (1 / _p2_.temp)`. The method should return the acceptance probability. 

The `acceptance_probability` method takes in three parameters: `_p1_`, `_p2_`, and `denom`. The `denom` parameter is used for normalizing the score difference. If `denom` is zero, the method should return 0.
"""

import numpy as np

def acceptance_probability(_p1_, _p2_, denom):
    """
    Calculate the acceptance probability for a potential solution based on the current and potential scores and temperatures.

    Parameters:
    _p1_ (object): The current solution.
    _p2_ (object): The potential solution.
    denom (float): The normalization factor for the score difference.

    Returns:
    float: The acceptance probability.
    """
    if denom == 0:
        return 0
    else:
        score_diff_norm = (_p1_.score_current - _p2_.score_current) / denom
        temp = (1 / _p1_.temp) - (1 / _p2_.temp)
        return np.exp(score_diff_norm * temp)