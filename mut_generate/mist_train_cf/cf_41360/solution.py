"""
QUESTION:
Implement a function `compute_eval_global(w_global, machines)` that computes the global evaluation based on local evaluations obtained from each machine. The function takes two parameters: `w_global`, the global parameter, and `machines`, a list of machine objects with `compute_eval` method. The function should return the global evaluation, which is the mean of the local evaluations if there are multiple machines, or the single local evaluation if there is only one machine.
"""

import numpy as np

def compute_eval_global(w_global, machines):
    local_evals = np.array([machine.compute_eval(w_global) for machine in machines])
    
    if local_evals.shape[0] == 1:
        eval_global = local_evals[0]
    else:
        eval_global = np.mean(local_evals, axis=0)
    
    return eval_global