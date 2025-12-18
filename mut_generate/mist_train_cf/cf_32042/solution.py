"""
QUESTION:
Implement a function called `filter_repositories` that takes a list of repository dictionaries, a keyword string, and a minimum number of stars integer as input. Each repository dictionary contains "reponame", "filename", and "gh_stars" keys. The function should return a list of repository dictionaries where the keyword is found in the repository name or file name, and the repository has at least the specified minimum number of stars.
"""

from typing import List, Dict, Union

def filter_repositories(repositories: List[Dict[str, Union[str, int]]], keyword: str, min_stars: int) -> List[Dict[str, Union[str, int]]]:
    filtered_repositories = []
    for repo in repositories:
        if keyword in repo["reponame"] or keyword in repo["filename"]:
            if repo["gh_stars"] >= min_stars:
                filtered_repositories.append(repo)
    return filtered_repositories