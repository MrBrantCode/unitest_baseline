"""
QUESTION:
Implement the `sample_orthogonalizer` function, which takes in the indices of the selected samples `idx`, the feature matrix `X_proxy`, the property matrix `Y_proxy`, and an optional tolerance value `tol`. The function should return the orthogonalized subset of `X_proxy` and `Y_proxy` with respect to the selected samples, where the orthogonalization process is performed using the Gram-Schmidt orthogonalization method. The function should be able to handle the case where the input matrices have the same number of columns as the length of the indices.
"""

import numpy as np

def sample_orthogonalizer(idx, X_proxy, Y_proxy, tol=1e-12):
    """
    Orthogonalizes two matrices, meant to represent a feature matrix
    :math:`{\\mathbf{X}}` and a property matrix :math:`{\\mathbf{Y}}`, given
    the selected samples :math:`{r}`

    Parameters:
    idx (array-like): Indices of the selected samples
    X_proxy (np.ndarray): Feature matrix X
    Y_proxy (np.ndarray): Property matrix Y
    tol (float): Tolerance value for numerical stability (default: 1e-12)

    Returns:
    np.ndarray, np.ndarray: Orthogonalized subset of X and Y matrices

    """
    # Select the subset of rows from X and Y based on the given indices
    X_selected = X_proxy[idx]
    Y_selected = Y_proxy[idx]

    # Compute the Gram-Schmidt orthogonalization of the selected subset of X with respect to the selected subset of Y
    Q, _ = np.linalg.qr(Y_selected.T)
    X_orthogonalized = X_selected - np.dot(np.dot(Q, Q.T), X_selected)

    return X_orthogonalized, Y_selected