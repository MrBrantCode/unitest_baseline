"""
QUESTION:
Implement a function named `getUpdateUrl` that takes two parameters: `tournament_id` and `match_id`. This function should return a string representing the URL for updating a match on the Challonge API, in the format `https://api.challonge.com/v1/tournaments/{tournament_id}/matches/{match_id}.json`. The returned URL should have the `{tournament_id}` and `{match_id}` placeholders replaced with the actual provided IDs.
"""

def getUpdateUrl(tournament_id, match_id):
    return f"https://api.challonge.com/v1/tournaments/{tournament_id}/matches/{match_id}.json"