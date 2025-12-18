"""
QUESTION:
Create a function named `get_rating` that takes a list of movie review comments as input. The function should return a rating based on the review comments. If a review comment contains both "highly recommended" and "disappointing", the rating should be 1. If a review comment contains only "highly recommended", the rating should be 5. If a review comment contains only "disappointing", the rating should be 2. For all other review comments, the rating should be 3.
"""

def get_rating(rev_comments):
    """
    This function calculates a rating based on the given movie review comments.

    Args:
    rev_comments (list): A list of movie review comments.

    Returns:
    int: The calculated rating.
    """
    rating = 3
    for comment in rev_comments:
        if "highly recommended" in comment and "disappointing" in comment:
            rating = 1
        elif "highly recommended" in comment:
            rating = 5
        elif "disappointing" in comment:
            rating = 2
    return rating