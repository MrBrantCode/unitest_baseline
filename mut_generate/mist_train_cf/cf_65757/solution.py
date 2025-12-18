"""
QUESTION:
Implement a function named `git_bisect` that takes in a list of commits and a function to check if a commit is good or bad. The function should use a binary search algorithm to find the first bad commit in the list. The function should return the index of the first bad commit.
"""

def git_bisect(commits, is_bad):
    """
    This function uses a binary search algorithm to find the first bad commit in the list.
    
    Args:
    commits (list): A list of commits.
    is_bad (function): A function to check if a commit is good or bad.
    
    Returns:
    int: The index of the first bad commit.
    """
    left, right = 0, len(commits) - 1
    while left < right:
        mid = (left + right) // 2
        if is_bad(commits[mid]):
            right = mid
        else:
            left = mid + 1
    return left