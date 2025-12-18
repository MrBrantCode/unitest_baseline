"""
QUESTION:
Write a function called `extract_constituents` that takes an array of integers and a threshold integer as input, and returns a new array containing the elements from the input array whose 1-based index is greater than the given threshold.
"""

def extract_constituents(arr, threshold):
    return [num for i, num in enumerate(arr, 1) if i > threshold]