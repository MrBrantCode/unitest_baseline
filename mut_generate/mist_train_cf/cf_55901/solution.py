"""
QUESTION:
Implement a custom kernel function for the Support Vector Machine (SVM) in Python, ensuring it satisfies Mercer's Theorem. The custom kernel function should take two parameters, X and Y, and return a value representing the similarity between the vectors in a higher-dimensional space. Use the custom kernel function with the scikit-learn SVM Classifier.
"""

import numpy as np

def entrance(X, Y):
    """
    Custom kernel function for Support Vector Machine (SVM).
    
    Parameters:
    X (array-like): Input data.
    Y (array-like): Input data.
    
    Returns:
    array-like: The similarity between the vectors in a higher-dimensional space.
    """
    return np.dot(X, Y.T)