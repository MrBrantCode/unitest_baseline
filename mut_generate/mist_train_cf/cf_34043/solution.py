"""
QUESTION:
Write a function `highest_priority_repository` that takes a list of repository strings in the format "name-priority", where "name" is the repository name and "priority" is a numerical value indicating its priority. The function should return the name of the repository with the highest priority. The priority values are integers and can be positive or negative. The list of repositories is non-empty and contains at least one valid repository string.
"""

from typing import List

def highest_priority_repository(repositories: List[str]) -> str:
    max_priority = float('-inf')
    max_repo_name = ''
    
    for repo in repositories:
        name, priority = repo.split('-')
        priority = int(priority)
        if priority > max_priority:
            max_priority = priority
            max_repo_name = name
    
    return max_repo_name