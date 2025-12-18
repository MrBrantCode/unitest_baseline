"""
QUESTION:
Implement a function `knn` that takes in three parameters: the number of nearest neighbors `k`, a list of data points `data`, a list of corresponding labels `targets`, and a query point `query`. The function should return the most common label among the `k` nearest neighbors to the query point.
"""

import heapq

def get_neighbors(k, data, query):
    return heapq.nsmallest(k, range(len(data)), key=lambda i: ((data[i][0]-query[0])**2 + (data[i][1]-query[1])**2)**0.5)

def knn(k, data, targets, query):
    indices = get_neighbors(k, data, query)
    counts = {}
    for index in indices:
        label = targets[index]
        counts[label] = counts.get(label, 0) + 1
    labels = sorted(counts, key=counts.get, reverse=True)
    return labels[0]