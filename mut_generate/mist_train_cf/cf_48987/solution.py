"""
QUESTION:
Create a function `smallest_threshold` that takes a list of floating point numbers and a threshold as arguments. The function should return the smallest non-negative number from the list that is also larger than the provided threshold. If no such number exists, the function should return `None`.
"""

def smallest_threshold(lst, threshold):
    # Filtering non-negative elements larger than threshold
    positives = [n for n in lst if n >= 0 and n > threshold]
    
    # If there are such elements
    if positives:
        return min(positives)
    
    return None