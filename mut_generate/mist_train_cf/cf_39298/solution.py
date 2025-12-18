"""
QUESTION:
Implement a `calculate_distance` method in the `CosineDistance` class that calculates the Negated Mahalanobis Cosine Distance between two input vectors `p` and `q` using a given Mahalanobis matrix `M`. The Negated Mahalanobis Cosine Distance is defined as:
\[ d(p, q) = -\frac{(p - q)^T \cdot M \cdot (p - q)}{\|p\| \cdot \|q\|} \]
where `p` and `q` are input vectors, `M` is the Mahalanobis matrix, `^T` denotes the transpose of a matrix, and `||.||` denotes the Euclidean norm of a vector. The input vectors `p` and `q` are array-like and the Mahalanobis matrix `M` is a predefined matrix. The method should return the calculated Negated Mahalanobis Cosine Distance as a float value.
"""

def calculate_distance(p, q, M):
    """
    Calculate the Negated Mahalanobis Cosine Distance between two input vectors p and q.

    Args:
    p (array-like): Input vector p
    q (array-like): Input vector q
    M (array-like): Mahalanobis matrix

    Returns:
    float: Negated Mahalanobis Cosine Distance between vectors p and q
    """
    p = np.asarray(p).flatten()
    q = np.asarray(q).flatten()
    mahalanobis_term = np.dot(np.dot((p - q), M), (p - q))
    norm_p = np.linalg.norm(p)
    norm_q = np.linalg.norm(q)
    distance = -mahalanobis_term / (norm_p * norm_q)
    return distance