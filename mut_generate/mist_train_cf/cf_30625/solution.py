"""
QUESTION:
Write a function `count_label_types(label_kinds)` that takes a list of label types as input, where each type is represented as a string, and returns a dictionary containing the count of each unique label type. The function should handle different label types case sensitively.
"""

def count_label_types(label_kinds):
    label_counts = {}
    for label in label_kinds:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    return label_counts