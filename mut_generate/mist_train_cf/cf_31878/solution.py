"""
QUESTION:
Implement the function `adaGradUpdate(params, grad, g, g2, mem, fixedRate, bestIter, r)` that takes in the current parameters `params`, gradients `grad`, and other relevant variables, and returns the updated parameters after applying the AdaGrad update rule.

The function should apply the following AdaGrad update rules:
- Update `g2` using the formula: `g2 = (1-r)*g2 + r*grad**2`.
- Calculate the learning rate `rate` using the formula: `rate = g*g/(g2+1e-16)`.
- Update the memory variable `mem` using the formula: `mem *= (1 - rate)`.
- Calculate the learning rate `learningRate` using the formula: `learningRate = fixedRate/(max(bestIter, 7))`.
- Update the memory variable `mem` using the formula: `mem += 1`.
- Calculate the update factor `alpha` using the formula: `alpha = np.minimum(learningRate, rate)/(np.sqrt(g2)+1e-16)`.
- Update the parameters using the formula: `params = params - grad*alpha`.

The function should return the updated parameters as a numpy array.
"""

import numpy as np

def adaGradUpdate(params, grad, g, g2, mem, fixedRate, bestIter, r) -> np.ndarray:
    """
    This function applies the AdaGrad update rule to the given parameters.

    Args:
    params (np.ndarray): The current parameters.
    grad (np.ndarray): The gradients.
    g (float): A variable used in the calculation of the learning rate.
    g2 (float): A variable used in the calculation of the learning rate.
    mem (float): A memory variable.
    fixedRate (float): A fixed learning rate.
    bestIter (int): The best iteration.
    r (float): A variable used in the calculation of g2.

    Returns:
    np.ndarray: The updated parameters.
    """
    g2 = (1-r)*g2 + r*grad**2
    rate = g*g/(g2+1e-16)
    mem *= (1 - rate)
    learningRate = fixedRate/(max(bestIter, 7))
    mem += 1
    alpha = np.minimum(learningRate, rate)/(np.sqrt(g2)+1e-16)
    return params - grad*alpha