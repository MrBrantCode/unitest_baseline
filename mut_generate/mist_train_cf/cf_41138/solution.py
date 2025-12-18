"""
QUESTION:
Implement a function `get_unique_labels(labels_data)` that takes a list of labels `labels_data` as input and returns a list of unique labels in the order they first appear. The function should not include duplicate labels and should maintain the original order of the labels. The input list `labels_data` is not guaranteed to be sorted or contain distinct elements.
"""

def get_unique_labels(labels_data):
    unique_labels = []
    seen_labels = set()
    for label in labels_data:
        if label not in seen_labels:
            unique_labels.append(label)
            seen_labels.add(label)
    return unique_labels