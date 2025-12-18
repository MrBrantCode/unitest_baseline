"""
QUESTION:
Create a function `k_NN(k, x_test, dataset)` that implements the k-Nearest Neighbors (k-NN) algorithm to categorize the outcome as "positive" or "negative" based on the provided dataset. The function should take three parameters: `k` as the number of nearest neighbors to consider, `x_test` as the input data to be classified, and `dataset` as the training dataset.

The function should return the predicted outcome for each input in `x_test` based on the majority vote of the k-nearest neighbors. The dataset is expected to have the features in the first columns and the target outcome in the last column.

Restrictions: The function should use the Euclidean distance to calculate the distance between data points and should sort the distances to find the k-nearest neighbors.
"""

import pandas as pd
import numpy as np
from collections import Counter

def k_NN(k, x_test, dataset):
    # Parser
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    
    # Algorithm
    predictions = []
    for x_t in x_test:
        distance = []
        for j in range(len(x)):
            dist = np.sqrt(np.sum(np.square(x_t - x[j])))
            distance.append((dist, j))
        distance.sort(key=lambda x: x[0])

        neighbors = []
        for l in range(k):
            neighbors.append(y[distance[l][1]])
        
        prediction = Counter(neighbors).most_common(1)[0][0]
        predictions.append(prediction)
    
    return predictions