"""
QUESTION:
Implement the `grad_num` function to numerically differentiate a given function `fn` with respect to its argument `arg` using the central difference method. The function `arg` can be a numpy array of arbitrary shape, and `step_size` can be a number or an array of the same shape as `arg`. The function should return the numerical gradient of `fn` with respect to `arg`.
"""

import numpy as np

def grad_num(fn, arg, step_size=1e-7):
    """ Numerically differentiate `fn` w.r.t. its argument `arg` 
    `arg` can be a numpy array of arbitrary shape
    `step_size` can be a number or an array of the same shape as `arg` """
    
    # Initialize an array to store the numerical gradient
    grad = np.zeros_like(arg)
    
    # Iterate over each element of the argument array
    it = np.nditer(arg, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        
        # Store the original value of the argument at the current index
        original_value = arg[idx]
        
        # Perturb the argument value slightly forward and backward
        arg[idx] = original_value + step_size
        fn_forward = fn(arg)
        
        arg[idx] = original_value - step_size
        fn_backward = fn(arg)
        
        # Calculate the numerical gradient using the central difference method
        grad[idx] = (fn_forward - fn_backward) / (2 * step_size)
        
        # Reset the argument value to its original value
        arg[idx] = original_value
        
        it.iternext()
    
    return grad