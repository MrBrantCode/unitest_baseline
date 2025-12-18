"""
QUESTION:
Create a function called `classify_birds` that takes a list of bird species data as input. The data is stored as a list of dictionaries where each dictionary represents one bird and its features. The function should use a for loop to create a 2D matrix containing the features of each bird and a list called `bird_labels` containing the classification label of each bird every 15 birds. The function should return the matrix and `bird_labels` as numpy arrays. The input list is expected to have a length that is a multiple of 15. The matrix should have a shape of (len(birds), 3), where each row represents a bird and each column represents a feature (beak length, wing span, and body mass).
"""

import numpy as np

def classify_birds(birds):
    num_features = 3
    birds_per_label = 15
    matrix = np.zeros((len(birds), num_features))
    labels = []
    
    for i, bird in enumerate(birds):
        matrix[i,:] = [bird["beak_length"], bird["wing_span"], bird["body_mass"]]
        if i % birds_per_label == 0:
            labels.append(bird["class"])
            
    return np.array(matrix), np.array(labels)