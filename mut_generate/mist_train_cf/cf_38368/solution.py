"""
QUESTION:
Implement the `ann` function to perform the Maximal Inner Product Search (MIPS) algorithm. The function should take query vectors `qy`, database vectors `db`, and the value of `k` as input, and return the indices of the `k` database vectors that maximize the inner product with each query vector. The implementation should use efficient vectorized operations.
"""

import numpy as np

def ann(qy, db, k):
    # Calculate the inner product matrix between query and database vectors
    inner_products = np.dot(qy, db.T)
    
    # Find the indices of the top k inner products for each query vector
    top_k_indices = np.argsort(-inner_products, axis=1)[:, :k]
    
    return top_k_indices