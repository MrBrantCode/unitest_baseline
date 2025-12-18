"""
QUESTION:
Create a function `countRepositories` that takes two parameters: a list of integers representing the number of stars for each GitHub repository, and a string representing the range of stars to analyze in the format "min-max". The function should return the count of repositories whose star count falls within the specified range.
"""

def countRepositories(stars, star_range):
    min_stars, max_stars = map(int, star_range.split('-'))
    return sum(1 for star in stars if min_stars <= star <= max_stars)