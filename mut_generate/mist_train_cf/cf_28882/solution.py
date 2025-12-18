"""
QUESTION:
Implement a function `get_leaderboard_page(queryset, offset, LEADERBOARD_MAX_PER_PAGE)` to retrieve a specific page of results from a leaderboard system. The function should take a list of player scores (`queryset`), a starting index (`offset`), and the maximum number of entries per page (`LEADERBOARD_MAX_PER_PAGE`) as input. It should return the subset of scores for the specified page. If the offset exceeds the length of the queryset, return an empty list.
"""

def get_leaderboard_page(queryset, offset, LEADERBOARD_MAX_PER_PAGE):
    start_index = offset
    end_index = offset + LEADERBOARD_MAX_PER_PAGE
    return queryset[start_index:end_index]