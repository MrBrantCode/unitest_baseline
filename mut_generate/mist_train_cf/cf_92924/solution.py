"""
QUESTION:
Write a function named `dataset_to_matrix` that transforms a dataset of tuples into a matrix. Each tuple represents a data point and contains three elements: two features and one label. The function should return a list of lists, where each sublist represents a row in the matrix. The function should only include tuples with exactly three elements in the matrix.
"""

def dataset_to_matrix(dataset):
    matrix = []
    for data_point in dataset:
        if len(data_point) == 3:  # Only consider tuples with three elements
            row = list(data_point)
            matrix.append(row)
    return matrix