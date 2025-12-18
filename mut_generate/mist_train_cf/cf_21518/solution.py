"""
QUESTION:
Transform a dataset of 3-element tuples into a matrix where each row represents a data point followed by its label. The function should be named `transform_dataset` and take a list of tuples as input. If the input dataset is empty, the function should return an empty list. If any tuple in the dataset has less than 3 elements, the function should raise an exception indicating an invalid dataset.
"""

def transform_dataset(dataset):
    if len(dataset) == 0:
        return []
    
    matrix = []
    for data in dataset:
        if len(data) < 3:
            raise Exception("Invalid dataset")
        matrix.append(list(data))
    
    return matrix