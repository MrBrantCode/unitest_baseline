"""
QUESTION:
Given a list of integers representing the scores of all players in a game, write a function named `count_eligible_players` that returns the number of players who can play the game, where a player can only play if their score is greater than the average score of all players. The input list `scores` contains integers between 0 and 100, inclusive, and has a length between 1 and 10^5.
"""

from typing import List

def count_eligible_players(scores: List[int]) -> int:
    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    eligible_players = sum(1 for score in scores if score > average_score)
    return eligible_players