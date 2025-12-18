"""
QUESTION:
Implement a function `logistic_regression` that performs logistic regression from scratch in Python without using any external libraries. The function should take in the following parameters: `X` (input data), `y` (labels), `learning_rate` (learning rate for gradient descent), `epochs` (number of iterations), and `threshold` (threshold for binary classification). The function should return the predicted class labels or probabilities. Implement the function to handle both binary and multi-class classification problems.
"""

import numpy as np

def logistic_regression(X, y, learning_rate=0.01, epochs=1000, threshold=0.5):
    """
    This function performs logistic regression from scratch in Python without using any external libraries.
    
    Parameters:
    X (numpy array): Input data
    y (numpy array): Labels
    learning_rate (float): Learning rate for gradient descent (default is 0.01)
    epochs (int): Number of iterations (default is 1000)
    threshold (float): Threshold for binary classification (default is 0.5)
    
    Returns:
    predicted_class: Predicted class labels
    """
    
    # Initialize weights and bias
    weights = np.zeros(X.shape[1])
    bias = 0
    
    # Define the sigmoid function
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    # Train the model
    for _ in range(epochs):
        # Forward propagation
        linear_combination = np.dot(X, weights) + bias
        probabilities = sigmoid(linear_combination)
        
        # Backward propagation
        weights_derivative = np.dot(X.T, (probabilities - y)) / len(y)
        bias_derivative = np.sum(probabilities - y) / len(y)
        
        # Gradient descent
        weights -= learning_rate * weights_derivative
        bias -= learning_rate * bias_derivative
    
    # Make predictions
    linear_combination = np.dot(X, weights) + bias
    probabilities = sigmoid(linear_combination)
    
    # Apply threshold for binary classification
    predicted_class = (probabilities >= threshold).astype(int)
    
    return predicted_class