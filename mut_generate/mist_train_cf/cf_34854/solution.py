"""
QUESTION:
Implement a Python function `update_function_array(function_array, nmax, theta)` that takes a 3D NumPy array `function_array` with shape `(nmax+1, nmax+1, nmax+1)`, an integer `nmax`, and a 1D NumPy array `theta` with shape `(m,)` as input. Update the `function_array` based on mathematical calculations involving the indices and `theta`, and return the updated array.
"""

import numpy as np

def update_function_array(function_array, nmax, theta):
    index = np.arange(nmax + 1)
    function_array[:, index[2:], index[1:-1]] = np.sqrt(2 * index[2:] + 1) * np.cos(theta[:, np.newaxis]) * \
                                                function_array[:, index[1:-1], index[1:-1]]

    for row in range(2, nmax + 1):
        n = index[row:]
        m = index[0:-row]
        function_array[:, n, m] = np.sqrt((2.0 * n - 1.0) / (n - m) * (2.0 * n + 1.0) / (n + m)) * \
                                  np.cos(theta[:, np.newaxis]) * function_array[:, n - 1, m] - \
                                  np.sqrt((2.0 * n + 1.0) / (2.0 * n - 3.0) * (n - m - 1.0) / (n - m) *
                                          (n + m - 1.0) / (n + m)) * function_array[:, n - 2, m]

    return function_array