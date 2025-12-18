"""
QUESTION:
Create a function called `calculate_player_performance` that takes a list of dictionaries as input, where each dictionary contains the keys "name", "hits", "at_bats", and "rbis", representing a player's name, number of hits, number of at-bats, and number of runs batted in (RBIs) respectively. The function should calculate each player's performance rating using the formula: (Hits + RBIs) / At-Bats * 100, and return a dictionary with each player's name as the key and their performance rating as the value. The performance rating should be rounded to two decimal places.
"""

from typing import List, Dict, Union

def calculate_player_performance(player_stats: List[Dict[str, Union[str, int]]]) -> Dict[str, float]:
    performance_ratings = {}
    for player in player_stats:
        hits = player["hits"]
        at_bats = player["at_bats"]
        rbis = player["rbis"]
        performance_rating = (hits + rbis) / at_bats * 100
        performance_ratings[player["name"]] = round(performance_rating, 2)
    return performance_ratings