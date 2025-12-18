"""
QUESTION:
Implement a function `calculate_new_ratings` that takes two lists of tuples `winners` and `losers` as input, where each tuple represents a player's information in the format `(player, rating, rd)`. The function should calculate the new ratings for the players based on the Elo rating system and return a list of tuples containing the player object and their new rating after the matches. 

Assume the Elo rating system formula is used with a constant K, and the rating deviation is adjusted by a constant factor. The expected score for each player is calculated based on their opponents' ratings, and the actual score is 1 for winners and 0 for losers.
"""

import math

def calculate_new_ratings(winners, losers):
    K = 32  
    new_ratings = []

    for winner in winners:
        total_losers_rating = sum(loser[1] for loser in losers)
        expected_score = 1 / (1 + 10 ** ((total_losers_rating - winner[1]) / 400))
        actual_score = 1  
        rating_change = K * (actual_score - expected_score)
        new_rating = winner[1] + rating_change
        new_rd = math.sqrt(winner[2] ** 2 + 50 ** 2)  
        new_ratings.append((winner[0], new_rating, new_rd))

    for loser in losers:
        total_winners_rating = sum(winner[1] for winner in winners)
        expected_score = 1 / (1 + 10 ** ((total_winners_rating - loser[1]) / 400))
        actual_score = 0  
        rating_change = K * (actual_score - expected_score)
        new_rating = loser[1] + rating_change
        new_rd = math.sqrt(loser[2] ** 2 + 50 ** 2)  
        new_ratings.append((loser[0], new_rating, new_rd))

    return new_ratings