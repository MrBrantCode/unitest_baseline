"""
QUESTION:
Create a function `count_profile_pictures_by_month` that takes a list of ProfilePicture objects as input and returns a dictionary where the keys are the month-year combinations (e.g., "Jan-2022") and the values are the counts of profile pictures created in that month-year. The keys in the dictionary should be sorted in chronological order.
"""

from typing import List, Dict
from collections import defaultdict
import datetime

def count_profile_pictures_by_month(profile_pictures: List[object]) -> Dict[str, int]:
    counts_by_month = defaultdict(int)
    for picture in profile_pictures:
        month_year = picture.created_at.strftime("%b-%Y")
        counts_by_month[month_year] += 1
    return dict(sorted(counts_by_month.items()))