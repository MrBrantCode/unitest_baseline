"""
QUESTION:
Implement a Naive Bayes classifier in Python, `NaiveBayes`, with Laplace smoothing to handle zero probabilities. The classifier should also handle missing values in the dataset using mean imputation. The `NaiveBayes` class should have a `fit` method to train the model and a `predict` method to make predictions on new data. The input data should be a 2D array with features, and the labels should be a 1D array. Missing values in the dataset should be represented as NaN.
"""

import numpy as np

def NaiveBayes(X, y):
    classes = np.unique(y)
    class_probs = np.zeros(len(classes))
    feature_probs = {}
    feature_means = {}

    for i, c in enumerate(classes):
        X_c = X[y == c]
        class_probs[i] = len(X_c) / len(X)

        feature_probs[c] = {}
        feature_means[c] = np.nanmean(X_c, axis=0)

        for j in range(X.shape[1]):
            feature_values = np.unique(X_c[:, j])
            feature_probs[c][j] = {}

            for value in feature_values:
                count = np.sum(X_c[:, j] == value)
                feature_probs[c][j][value] = (count + 1) / (len(X_c) + len(feature_values))

    def predict(X):
        predictions = []
        for x in X:
            class_scores = []
            for i, c in enumerate(classes):
                score = np.log(class_probs[i])
                for j, value in enumerate(x):
                    if np.isnan(value):
                        value = feature_means[c][j]
                    if value in feature_probs[c][j]:
                        score += np.log(feature_probs[c][j][value])
                    else:
                        score += np.log(1 / (len(feature_probs[c][j]) + 1))  # Laplace smoothing
                class_scores.append(score)
            predictions.append(classes[np.argmax(class_scores)])
        return predictions
    return predict