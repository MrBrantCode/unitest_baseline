"""
QUESTION:
Write a function named `calculate_percentile_rank` that takes a list of integers representing student test scores as input. The function should calculate the median score and then determine the percentile rank of the median score using a binary search algorithm. The function should return the percentile rank as a float value between 0 and 1. The input list is guaranteed to be non-empty.
"""

def calculate_percentile_rank(scores):
    """
    Calculate the percentile rank of the median score in a list of scores.
    
    Args:
    scores (list): A list of integers representing student test scores.
    
    Returns:
    float: The percentile rank of the median score as a float value between 0 and 1.
    """
    
    # Sort the list of scores
    sorted_scores = sorted(scores)
    
    # Calculate the median score
    n = len(sorted_scores)
    median_score = sorted_scores[n // 2] if n % 2 != 0 else (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
    
    # Perform binary search to find the position of the median score
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_scores[mid] < median_score:
            low = mid + 1
        elif sorted_scores[mid] > median_score:
            high = mid - 1
        else:
            break
    
    # Calculate the percentile rank
    percentile_rank = (mid + 1) / n
    
    return percentile_rank