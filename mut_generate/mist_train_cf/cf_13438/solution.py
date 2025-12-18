"""
QUESTION:
Implement a function named `naive_bayes_classifier` that calculates the probability of a particular class given a set of features using Bayes' theorem. The function should take in the following parameters: `features`, `class_probabilities`, `feature_probabilities_given_class`, and `class_priors`. The function should return a dictionary with the predicted class and its corresponding probability. The function should assume that the presence of a particular feature is independent of the presence of other features.

Note: Do not use any external libraries such as scikit-learn. Implement the Naive Bayes classifier from scratch.
"""

def naive_bayes_classifier(features, class_probabilities, feature_probabilities_given_class, class_priors):
    """
    This function calculates the probability of a particular class given a set of features using Bayes' theorem.

    Args:
    features (list): A list of features.
    class_probabilities (dict): A dictionary where the keys are the classes and the values are their corresponding probabilities.
    feature_probabilities_given_class (dict): A dictionary where the keys are the classes and the values are dictionaries with the feature probabilities given the class.
    class_priors (dict): A dictionary where the keys are the classes and the values are their corresponding prior probabilities.

    Returns:
    dict: A dictionary with the predicted class and its corresponding probability.
    """

    # Initialize a dictionary to store the probabilities of each class given the features
    probabilities = {}

    # Calculate the probability of each class given the features
    for class_ in class_probabilities:
        # Calculate the probability of the features given the class
        feature_probability_given_class = 1
        for feature in features:
            feature_probability_given_class *= feature_probabilities_given_class[class_][feature]

        # Calculate the probability of the class given the features using Bayes' theorem
        probability = (feature_probability_given_class * class_priors[class_]) / class_probabilities[class_]
        probabilities[class_] = probability

    # Predict the class with the highest probability
    predicted_class = max(probabilities, key=probabilities.get)

    return {"class": predicted_class, "probability": probabilities[predicted_class]}