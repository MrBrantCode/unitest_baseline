"""
QUESTION:
Complete the implementation of the ALS update step for matrix factorization by writing the missing code for the convergence check and normalization step.

Given variables: 
- U: A matrix representing user latent factors
- U_old: The previous state of matrix U
- V: A matrix representing item latent factors
- V_old: The previous state of matrix V
- is_convergence: A boolean variable indicating whether the algorithm has converged

Restrictions:
- Use the provided functions: np.dot(A, B), A.transpose(), A ** 2, math.sqrt(x), abs(x), and sum(axis=0) 
- The convergence check should be based on the absolute sum of differences between the current and previous states of matrices U and V.
- The normalization step should be performed on matrix U by dividing each column by the square root of the element-wise sum along the columns of U squared.
"""

import numpy as np
import math

def als_update_step(U, U_old, V, V_old):
    # Complete the convergence check
    is_convergence = abs((U - U_old).sum()) < 0.01 and abs((V - V_old).sum()) < 0.01

    # Implement the normalization step for matrix U
    u_pow_2 = (U ** 2).sum(axis=0) 
    u_sqrt_pow_2 = np.array([math.sqrt(w) for w in u_pow_2])
    U = U / u_sqrt_pow_2

    return is_convergence, U