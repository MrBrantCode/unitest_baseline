"""
QUESTION:
Write a Python function `sanitize_dataset` that takes a 2-dimensional list `dataset` as input, attempts to convert each string entry into a float, and replaces non-numerical entries with 'N/A'. The function should modify the input dataset in-place and return the sanitized dataset.
"""

def sanitize_dataset(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            try:
                # Try to convert to float
                dataset[i][j] = float(dataset[i][j])
            except ValueError:
                # If fails to convert to float, replace with 'N/A'
                dataset[i][j] = 'N/A'
    return dataset