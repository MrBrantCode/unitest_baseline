"""
QUESTION:
Create a function `get_review_date(last_review, difficulty)` that takes in a date (`last_review`) and an integer (`difficulty`) representing the difficulty level of the material (0-4) and returns the next review date based on the following intervals:
- If difficulty is 0, review in 1 day
- If difficulty is 1, review in 3 days
- If difficulty is 2, review in 7 days
- If difficulty is 3, review in 14 days
- If difficulty is 4, review in 30 days
- For any other difficulty level, review in 60 days.
"""

import datetime

def get_review_date(last_review, difficulty):
    """
    Calculates the next review date based on the last review date and difficulty level.
    """
    if difficulty == 0:
        return last_review + datetime.timedelta(days=1)
    elif difficulty == 1:
        return last_review + datetime.timedelta(days=3)
    elif difficulty == 2:
        return last_review + datetime.timedelta(days=7)
    elif difficulty == 3:
        return last_review + datetime.timedelta(days=14)
    elif difficulty == 4:
        return last_review + datetime.timedelta(days=30)
    else:
        return last_review + datetime.timedelta(days=60)