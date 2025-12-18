"""
QUESTION:
Implement the function `simulate_system(A, B, C, x0, u, w, v)` that simulates a simple linear dynamical system. The function takes the system matrices `A`, `B`, and `C`, the initial state `x0`, the control input `u`, and the noise vectors `w` and `v`, and returns the simulated output `y` at each time step. `A`, `B`, and `C` are numpy arrays representing the system matrices, `x0` is a numpy array representing the initial state vector, `u` is a numpy array representing the control input vector, and `w` and `v` are numpy arrays representing the process and measurement noise vectors, respectively. Assume that the dimensions of the matrices and vectors are compatible for the given operations.
"""

import numpy as np

def simulate_system(A, B, C, x0, u, w, v):
    num_steps = u.shape[0]
    state_dim = x0.shape[0]
    output_dim = C.shape[0]

    x = np.zeros((num_steps + 1, state_dim))
    y = np.zeros((num_steps, output_dim))

    x[0] = x0
    for t in range(num_steps):
        x[t + 1] = A @ x[t] + B @ u[t] + w[t]
        y[t] = C @ x[t + 1] + v[t]

    return y