"""
QUESTION:
Create a function `analyzeAvailability` that takes a list of `Month` objects as input, where each `Month` object has `year` and `month` attributes, and returns a dictionary where the keys are the years and the values are lists of available months for each year. The function should group the months by their corresponding years.
"""

from typing import List, Dict

class Month:
    def __init__(self, year: int, month: str):
        self.year = year
        self.month = month

def analyzeAvailability(months: List[Month]) -> Dict[int, List[str]]:
    availability = {}
    for month in months:
        if month.year in availability:
            availability[month.year].append(month.month)
        else:
            availability[month.year] = [month.month]
    return availability