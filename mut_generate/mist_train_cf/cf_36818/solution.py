"""
QUESTION:
Write a Python function `process_training_data(features, targets, i_train)` that takes in a list of lists `features`, a list of target values `targets`, and a list of indices `i_train`. The function should return a tuple containing a list of features and a list of targets, both selected based on the indices in `i_train`. If only one feature is available for training, the function should return this feature as a single element rather than a list of lists.
"""

def process_training_data(features, targets, i_train):
    features_train = [features[i] for i in i_train]
    targets_train = [targets[i] for i in i_train]
    if len(features_train) == 1:
        features_train = features_train[0]
    return features_train, targets_train