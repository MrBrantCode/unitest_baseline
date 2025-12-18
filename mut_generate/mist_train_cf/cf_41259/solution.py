"""
QUESTION:
Implement a function `linear_regression_train` that trains a linear regression model using gradient descent. The function should take as input the input features (`features`), target values (`targets`), number of epochs (`num_epoch`), and learning rate (`learning_rate`). It should return the trained weights (`w`) and bias (`b`) after `num_epoch` iterations. The input features should be a 2D array where each row represents a data point and each column represents a feature, and the target values should be a 1D array.
"""

import numpy as np

def linear_regression_train(features, targets, num_epoch, learning_rate):
    # Initialize weights and bias
    w, b = np.zeros(features.shape[1]), 0
    
    # Gradient descent
    for e in range(num_epoch):
        # Forward pass
        predictions = np.dot(features, w) + b
        
        # Compute mean squared error loss
        loss = np.mean((predictions - targets) ** 2)
        
        # Compute gradients
        dw = 2 * np.dot(features.T, (predictions - targets)) / features.shape[0]
        db = 2 * np.mean(predictions - targets)
        
        # Update weights and bias
        w -= learning_rate * dw
        b -= learning_rate * db
    
    return w, b