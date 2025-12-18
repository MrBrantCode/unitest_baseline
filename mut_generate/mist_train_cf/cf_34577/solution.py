"""
QUESTION:
Implement the `train_perceptron` function, which trains the perceptron using the provided training dataset. The function takes four parameters: `train_features` (a 2D numpy array containing the training features), `train_labels` (a 1D numpy array containing the corresponding training labels), `class_labels` (a tuple containing the class labels), and `num_features` (an integer representing the number of features in the training dataset). The function should initialize the weight vector `theta` to a numpy array of zeros with a length equal to the number of features, then iterate over the training dataset and update the weight vector `theta` based on misclassified samples until convergence or a maximum number of iterations is reached.
"""

import numpy as np

def train_perceptron(train_features, train_labels, class_labels, num_features):
    NO_MAX_ITERATIONS = 20
    np.random.seed(0)

    theta = np.zeros(num_features)

    for _ in range(NO_MAX_ITERATIONS):
        misclassified = False
        for i in range(len(train_features)):
            x = train_features[i]
            y = train_labels[i]
            if y * np.dot(theta, x) <= 0:  # Misclassified sample
                theta = theta + y * x
                misclassified = True
        if not misclassified:
            break

    return theta