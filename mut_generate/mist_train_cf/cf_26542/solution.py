"""
QUESTION:
Create a function `preprocess_data(features, labels)` that takes in a list of features and a list of corresponding labels, and splits the data into batches of 4000 samples each. The remaining samples should be placed in a separate batch. The function should return a tuple containing two lists: the first list contains batches of features, and the second list contains batches of labels.
"""

def preprocess_data(features, labels):
    batch_size = 4000
    num_samples = len(features)
    
    num_batches = num_samples // batch_size
    remaining_samples = num_samples % batch_size
    
    features_batches = []
    labels_batches = []
    
    start_idx = 0
    for i in range(num_batches):
        end_idx = start_idx + batch_size
        features_batches.append(features[start_idx:end_idx])
        labels_batches.append(labels[start_idx:end_idx])
        start_idx = end_idx
    
    if remaining_samples > 0:
        features_batches.append(features[start_idx:])
        labels_batches.append(labels[start_idx:])
    
    return features_batches, labels_batches