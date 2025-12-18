"""
QUESTION:
Implement the `conjugate_gradient` function, which takes as input the matrix `A`, the vector `b`, an initial guess `x0`, a convergence threshold `eps`, and a maximum number of iterations `maxIter`. The function should return the solution vector `x` and the number of iterations performed `ite`. The `conjugate_gradient` function should solve the system of linear equations using the conjugate gradient method. The matrix `A` is assumed to be symmetric and positive-definite, and the function should stop iterating when the Euclidean norm of the residual is less than `eps`. The function should also be able to handle cases where the maximum number of iterations `maxIter` is reached.
"""

import numpy as np

def conjugate_gradient(A, b, x0, eps=1e-10, maxIter=1000):
    x = np.copy(x0)
    r = b - np.dot(A, x)
    p = np.copy(r)
    rsold = np.dot(r, r)

    for ite in range(maxIter):
        Ap = np.dot(A, p)
        alpha = rsold / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r, r)
        if np.sqrt(rsnew) < eps:
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew

    return x, ite+1