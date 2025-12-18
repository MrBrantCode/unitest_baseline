"""
QUESTION:
Implement a `NaiveBayes` function that takes as input a training dataset `X_train` and target values `y_train`, and returns a function that can predict the class label for new data points `X_test`. The function should assume conditional independence of features and a Gaussian distribution within each class.
"""

import numpy as np

# Calculate mean and std for each feature in each class
def summarize_by_class(X, y):
    classes = np.unique(y)
    summaries = {}
    for cls in classes:
        summaries[cls] = [(np.mean(X[y == cls, i]), np.std(X[y == cls, i])) for i in range(X.shape[1])]
    return summaries

# Calculate Gaussian probability density function
def gaussian_pdf(x, mean, std):
    exponent = np.exp(-((x-mean)**2 / (2 * std**2)))
    return (1 / (np.sqrt(2 * np.pi) * std)) * exponent

# Calculate class probabilities
def class_probabilities(summaries, x_test):
    total_rows = sum([len(summaries[label]) for label in summaries])
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = len(class_summaries) / float(total_rows)
        for i in range(len(class_summaries)):
            mean, std = class_summaries[i]
            probabilities[class_value] *= gaussian_pdf(x_test[i], mean, std)
    return probabilities

# Make predictions
def predict(summaries, x_test):
    probabilities = class_probabilities(summaries, x_test)
    best_label, best_prob = None, -1
    for cls, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = cls
    return best_label

def NaiveBayes(X_train, y_train):
    summaries = summarize_by_class(X_train, y_train)
    return lambda x_test: predict(summaries, x_test)