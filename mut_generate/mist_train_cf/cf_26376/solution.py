"""
QUESTION:
Implement a function `calculate_distances(dataset, query_point)` that takes in a 2D list `dataset` where each record is a list of four numerical values [class_label, feature1, feature2, feature3] and a list `query_point` with three numerical values [query_feature1, query_feature2, query_feature3]. The function should return a list of tuples, where each tuple contains the index of the record in the dataset and its corresponding Euclidean distance from the query point, sorted in ascending order based on the Euclidean distances.
"""

import math

def calculate_distances(dataset, query_point):
    distances = []
    for i, record in enumerate(dataset):
        class_label, feature1, feature2, feature3 = record
        euclidean_distance = math.sqrt((query_point[0] - feature1) ** 2 + (query_point[1] - feature2) ** 2 + (query_point[2] - feature3) ** 2)
        distances.append((i, euclidean_distance))
    distances.sort(key=lambda x: x[1])
    return distances