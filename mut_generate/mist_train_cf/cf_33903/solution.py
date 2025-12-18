"""
QUESTION:
Implement the Elo rating system by completing the following functions:

- `elo_prediction(home_rating, away_rating)`: Calculate the expected probability of the home team winning based on their Elo rating. The function should take two parameters, `home_rating` and `away_rating`, representing the Elo ratings of the home and away teams, respectively.
- `s_value(home_score, away_score)`: Calculate the result of the home and away teams' performance based on their scores. The function should take two parameters, `home_score` and `away_score`, representing the scores of the home and away teams, respectively.
- `k_factor(MOV, elo_diff)`: Calculate the K-factor for updating the Elo ratings of the home and away teams based on the margin of victory and the difference in Elo ratings. The function should take two parameters, `MOV` and `elo_diff`, representing the margin of victory and the difference in Elo ratings, respectively.
"""

import math

def elo_prediction(home_rating, away_rating):
    """
    Calculate the expected probability of the home team winning based on their Elo rating.
    """
    expected_home = 1 / (1 + math.pow(10, (away_rating - home_rating) / 400))
    return expected_home

### Required Function: s_value
def s_value(home_score, away_score):
    """
    Calculate the result of the home and away teams' performance based on their scores.
    """
    if home_score > away_score:
        return 1, 0  # Home team wins
    elif home_score < away_score:
        return 0, 1  # Away team wins
    else:
        return 0.5, 0.5  # Draw

### Required Function: k_factor
def k_factor(MOV, elo_diff):
    """
    Calculate the K-factor for updating the Elo ratings of the home and away teams based on the margin of victory and the difference in Elo ratings.
    """
    if MOV >= 0:
        home_k = 20 + (elo_diff / 20)
        away_k = 20 - (elo_diff / 20)
    else:
        home_k = 20 - (elo_diff / 20)
        away_k = 20 + (elo_diff / 20)
    return home_k, away_k