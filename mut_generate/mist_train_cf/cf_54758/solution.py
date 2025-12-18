"""
QUESTION:
Develop a function "median_score" that takes an array of scores and returns the median value. The array is not guaranteed to be sorted. The function should handle arrays of both even and odd lengths, calculating the median accordingly.
"""

def median_score(scores):
    scores.sort()
    length = len(scores)
    if length % 2 == 0:
        median = (scores[length//2] + scores[length//2 - 1]) / 2
    else:
        median = scores[length//2]
        
    return median