"""
QUESTION:
Create a function `get_review_date` that calculates the next review date based on the last review date and difficulty level. The function should take two parameters: `last_review` (a datetime.date object) and `difficulty` (an integer). The difficulty level determines the number of days until the next review, as follows: 

- difficulty 0: 1 day
- difficulty 1: 3 days
- difficulty 2: 7 days
- difficulty 3: 14 days
- difficulty 4: 30 days
- difficulty 5 or above: 60 days

The function should return a datetime.date object representing the next review date.
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