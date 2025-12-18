"""
QUESTION:
Given a list of unique integers representing player scores, write a function `calculateRanking(scores)` that takes the list as input and returns a list of integers representing the final ranking of the players in descending order of their scores. The input list `scores` will have a length between 1 and 100 (inclusive) and contain no ties. The output ranking list should have the player with the highest score ranked 1st, the next highest score ranked 2nd, and so on.
"""

def calculateRanking(scores):
    sorted_scores = sorted(enumerate(scores, 1), key=lambda x: x[1], reverse=True)
    ranking = [rank for rank, _ in sorted_scores]
    return ranking