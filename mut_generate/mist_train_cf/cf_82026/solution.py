"""
QUESTION:
Write a function named `underfitting_risk` that takes two parameters: `training_dataset_size` and `hypothesis_space_size`. The function should return `True` if the risk of underfitting is increased due to a large training dataset or an expansive hypothesis space, and `False` otherwise. Assume that a large training dataset is represented by a value greater than 1000, and an expansive hypothesis space is represented by a value greater than 100.
"""

def underfitting_risk(training_dataset_size, hypothesis_space_size):
    return training_dataset_size > 1000 or hypothesis_space_size > 100