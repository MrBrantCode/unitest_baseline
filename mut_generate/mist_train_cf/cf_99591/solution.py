"""
QUESTION:
Create a function called `get_review_date` that calculates the next review date based on the last review date and the difficulty level of the material. The difficulty level is an integer from 0 to 4, where 0 is the easiest and 4 is the hardest. The function should return the next review date as a datetime.date object, using the following rules: 
- If the difficulty level is 0, the next review date is 1 day after the last review date.
- If the difficulty level is 1, the next review date is 3 days after the last review date.
- If the difficulty level is 2, the next review date is 7 days after the last review date.
- If the difficulty level is 3, the next review date is 14 days after the last review date.
- If the difficulty level is 4, the next review date is 30 days after the last review date.
- If the difficulty level is greater than 4, the next review date is 60 days after the last review date.
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