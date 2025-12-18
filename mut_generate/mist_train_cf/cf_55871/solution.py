"""
QUESTION:
Write a function `calculate_career_stats` that takes a string `article` as input, parses it to extract the career average points and rebounds per game of Gordon Hayward, calculates the total points and rebounds in his career, and returns a dictionary containing the article, total points, and total rebounds. The function should handle cases where the extraction fails and return default values of 0 for total points and rebounds.
"""

import re

def calculate_career_stats(article):
    # Get points and rebounds from article
    points = re.search(r"(\d+\.\d+) points", article)
    rebounds = re.search(r"(\d+) rebounds", article)

    if points:
        average_points = float(points.group(1))
    else:
        average_points = 0

    if rebounds:
        average_rebounds = int(rebounds.group(1))
    else:
        average_rebounds = 0

    # Get career length
    years = re.search(r"(\d+)-year career", article)

    if years:
        career_years = int(years.group(1))
    else:
        career_years = 0

    # Calculate total points and rebounds
    total_points = average_points * career_years * 82  # 82 games in a season
    total_rebounds = average_rebounds * career_years * 82

    # Return the article, total points, and total rebounds
    return {
        "article": article,
        "total_points": total_points,
        "total_rebounds": total_rebounds
    }