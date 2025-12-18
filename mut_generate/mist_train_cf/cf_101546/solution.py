"""
QUESTION:
Create a function that takes a list of dictionaries representing bird species with their physical characteristics and a number of birds per label. The function should return a 2D numpy array of the birds' features and a numpy array of the corresponding classification labels. The 2D array should have a row for each bird and a column for each feature, and the labels array should have a label for every 15 birds. The function should use a for loop to iterate through the list of dictionaries and fill in the 2D array and labels array. The number of features per bird is 20.
"""

import numpy as np

def entrance(birds):
    num_features = 20
    birds_per_label = 15

    matrix = np.zeros((len(birds), num_features))
    labels = []

    for i, bird in enumerate(birds):
        features = [bird[key] for key in bird if key != 'class']
        matrix[i,:] = features
        if i % birds_per_label == 0:
            labels.append(bird["class"])

    return matrix, np.array(labels)