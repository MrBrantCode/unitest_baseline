"""
QUESTION:
Write a function named `count_unique_years` that takes a list of strings representing dates in the format "MM/DD/YYYY" and returns the count of unique years present in the list, ignoring any duplicate years.
"""

from typing import List

def entance(dateList: List[str]) -> int:
    unique_years = set()
    for date in dateList:
        year = date.split("/")[-1]
        unique_years.add(year)
    return len(unique_years)