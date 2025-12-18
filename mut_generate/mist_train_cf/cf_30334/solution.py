"""
QUESTION:
Implement the function calculate_new_rating(old_rating, result, opponent_rating, k_factor) that takes the old rating of a team, the result of a game, the opponent's rating, and the K-factor for the rating system, and returns the new rating of the team using the Elo rating system. The old rating and opponent's rating are between 1000 and 3000, the result is 1 for a win, 0.5 for a draw, or 0 for a loss, and the K-factor is between 10 and 100.
"""

def calculate_new_rating(old_rating: float, result: float, opponent_rating: float, k_factor: float) -> float:
    team_quotient = 10 ** (old_rating / 400)
    opponent_quotient = 10 ** (opponent_rating / 400)
    expected_result = team_quotient / (team_quotient + opponent_quotient)

    new_rating = old_rating + k_factor * (result - expected_result)
    return new_rating