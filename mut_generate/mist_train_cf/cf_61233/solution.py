"""
QUESTION:
Write a function `calculate_distance` that takes a sorted array `arr` and a target element `target` as input. The function should calculate and return the total distance between all occurrences of the target element within the array, handling separate clusters of the target element that are not adjacent. The distance within each cluster is calculated as the difference between the index of the last occurrence and the index of the first occurrence.
"""

def calculate_distance(arr, target):
    """
    Calculate the total distance between all occurrences of the target element within the array.
    
    Parameters:
    arr (list): A sorted array.
    target: The target element.
    
    Returns:
    int: The total distance between all occurrences of the target element.
    """
    clusters = []
    start = None
    for i, num in enumerate(arr):
        if num == target and start is None:
            start = i
        elif num != target and start is not None:
            clusters.append((start, i - 1))
            start = None
    if start is not None:
        clusters.append((start, len(arr) - 1))
        
    return sum(end - start for start, end in clusters)