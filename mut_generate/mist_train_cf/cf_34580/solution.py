"""
QUESTION:
Create a function `total_stars_for_checked_repositories` that takes a list of dictionaries representing GitHub repositories and a function that checks each repository, then returns the total number of stars for repositories that pass the check. Each repository dictionary must contain the keys "name", "stars", and "language". The check function must take a repository dictionary as input and return True if the repository passes the check, and False otherwise.
"""

def total_stars_for_checked_repositories(repos_list, check_function) -> int:
    return sum(repo["stars"] for repo in repos_list if check_function(repo))