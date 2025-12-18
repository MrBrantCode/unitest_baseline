"""
QUESTION:
Complete the function `multiply_orthonormal(q)` that takes a list `q` of vectors as input and returns a 2D list representing the unity matrix for an orthonormal system, where each vector in `q` is of unit length and orthogonal to every other vector in the set. The function should calculate the dot product of every vector in `q` with each vector in `q` and return a matrix where the dot product of orthogonal vectors is 0 and the dot product of a vector with itself is 1.
"""

def multiply_orthonormal(q):
    """
    Multiplies every object in q with each object in q. Should return a unity matrix for an orthonormal system.
    
    Args:
    q: A list of objects
    
    Returns:
    A 2D list representing the unity matrix for an orthonormal system
    """
    n = len(q)
    ret = [[0] * n for _ in range(n)]  # Initialize a 2D list with zeros
    
    for i in range(n):
        for j in range(n):
            dot_product = sum(q[i][k] * q[j][k] for k in range(len(q[i])))  # Calculate the dot product of vectors q[i] and q[j]
            ret[i][j] = dot_product  # Assign the dot product to the corresponding position in the result matrix
    
    return ret