"""
QUESTION:
Write a function named `find_most_starred_repo` that takes a list of dictionaries as input where each dictionary represents a GitHub repository with keys "name" (string), "owner" (string), and "stars" (integer). The function should return the name of the repository with the highest number of stars. If multiple repositories have the same highest number of stars, return the name of the first repository encountered in the list.
"""

def find_most_starred_repo(repos):
    max_stars = 0
    max_repo_name = ""
    for repo in repos:
        if repo["stars"] > max_stars:
            max_stars = repo["stars"]
            max_repo_name = repo["name"]
    return max_repo_name