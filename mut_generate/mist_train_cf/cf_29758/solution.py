"""
QUESTION:
Implement the function top_scores() that takes a list of lists representing student scores, a rank, and a subset size. The function should return a dictionary where each key is a student and each value is a list of their top subset size scores from rank onwards.

Restrictions:
- The rank and subset size should be 1-indexed.
- If the number of scores for a student is less than the specified subset size or rank, include all available scores in the subset.
- The scores should be sorted in descending order before selecting the subset.
- The top scores should also be in descending order.
"""

def top_scores(scores, rank, subset_size):
    """
    Returns a dictionary where each key is a student and each value is a list of their top subset size scores from rank onwards.
    
    Parameters:
    scores (dict): A dictionary where keys are students and values are lists of their scores.
    rank (int): The rank from which to consider scores (1-indexed).
    subset_size (int): The number of top scores to select (1-indexed).
    
    Returns:
    dict: A dictionary where each key is a student and each value is a list of their top subset size scores from rank onwards.
    """

    result = {}
    for student, student_scores in scores.items():
        # Sort the scores in descending order
        student_scores = sorted(student_scores, reverse=True)
        
        # Select the subset of scores from rank onwards
        subset = student_scores[rank-1:]
        
        # Select the top subset size scores
        top_scores = subset[:subset_size]
        
        # Store the top scores in the result dictionary
        result[student] = top_scores
    
    return result