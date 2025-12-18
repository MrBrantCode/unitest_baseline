"""
QUESTION:
Given a list of integers `values` where each element represents the worth of a sightseeing location, write a function `maxScoreSightseeingPair` that returns the maximum possible score that can be achieved from a pair of sightseeing spots. The score for a pair of sightseeing spots `i` and `j` is calculated as `values[i] + values[j] + i - j`. The function should take a list of integers as input and return an integer as output.

The constraints for this problem are: 
- The length of the `values` list is between 2 and 5 * 10^4 (inclusive).
- Each element in the `values` list is between 1 and 1000 (inclusive).
"""

def maxScoreSightseeingPair(values):
    max_seen = values[0] + 0  
    max_score = float('-inf')  

    for i in range(1, len(values)):
        current_score = max_seen + values[i] - i
        max_score = max(max_score, current_score)
        max_seen = max(max_seen, values[i] + i)

    return max_score