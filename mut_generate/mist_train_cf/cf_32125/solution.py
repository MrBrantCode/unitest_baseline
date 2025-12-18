"""
QUESTION:
Implement a `calculate_probability_of_inclusion` method in the `ProbabilityOfInclusionSVM` class that calculates the probability of inclusion for each data point in the trained SVM model. The method should take the trained SVM model `svm_model` and the training data `X_train` as input and return the probability of inclusion for each data point in `X_train`. The probability of inclusion should be calculated using the distance of each data point to the decision boundary of the SVM model.
"""

def calculate_probability_of_inclusion(svm_model, X_train):
    # Get the distance of each data point to the decision boundary
    decision_function = svm_model.decision_function(X_train)
    
    # Calculate the probability of inclusion for each data point
    distances = np.abs(decision_function)
    max_distance = np.max(distances)
    probabilities = 1 - (distances / max_distance)
    
    return probabilities