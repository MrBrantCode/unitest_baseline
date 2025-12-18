"""
QUESTION:
Implement a function called `process_features` that takes two parameters: a list of integers representing labels and a list of tuples, where each tuple contains an integer and a list of strings representing feature indexes and their values. The function should return a dictionary where the keys are the labels and the values are lists of corresponding features. The length of the labels and features lists will be between 1 and 10^5.
"""

from typing import List, Tuple, Dict

def process_features(labels: List[int], features: List[Tuple[int, List[str]]]) -> Dict[int, List[List[str]]]:
    result = {}
    for label, feature in zip(labels, features):
        if label in result:
            result[label].append(feature[1])
        else:
            result[label] = [feature[1]]
    return result