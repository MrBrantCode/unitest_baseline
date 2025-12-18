"""
QUESTION:
Implement a function `sort_labels` that takes a dictionary `plc` containing a list of labels as values for the key 'labels', and returns the sorted list of labels. The labels should be sorted in ascending order based on their alphanumeric values. If two labels have the same alphanumeric value, they should be sorted based on their original order in the input list. The function should be implemented using the following signature: `def sort_labels(plc: dict) -> List[str]`.
"""

from typing import List

def sort_labels(plc: dict) -> List[str]:
    labels = plc['labels']
    sorted_labels = sorted(labels, key=lambda x: ("".join(filter(str.isalpha, x)), labels.index(x)))
    return sorted_labels