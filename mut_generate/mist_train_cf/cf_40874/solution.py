"""
QUESTION:
Create a function `filter_repositories` that takes a list of GitHub repository tuples and a star count range string, and returns a filtered list of repository tuples within the specified range. The repository tuples contain a string for the repository name and an integer for the star count. The star count range string should be in the format "min-max". The function should return a list of tuples, where each tuple contains the repository name and its star count, and the star count falls within the specified range (inclusive).
"""

def filter_repositories(repositories, star_range):
    min_star, max_star = map(int, star_range.split('-'))
    return [(name, stars) for name, stars in repositories if min_star <= stars <= max_star]