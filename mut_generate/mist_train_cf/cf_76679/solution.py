"""
QUESTION:
Write a function called `find_indices` that takes a list of tuples and an integer `k` as input. The function should return the indices of the tuples where `k` is found. If `k` is not found in any tuple, it should return a custom error message. The function should also handle cases where the input is not a list of tuples or `k` is not an integer.
"""

def find_indices(tuples, k):
    if not isinstance(k, int):
        return "Error: Argument 'k' should be an integer"
    
    if not all(isinstance(t, tuple) for t in tuples):
        return "Error: All elements should be tuples"
    
    indices = [i for i, t in enumerate(tuples) if k in t]
    
    if not indices:
        return f"No tuples found containing the number {k}"
    
    return indices