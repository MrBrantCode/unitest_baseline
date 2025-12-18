"""
QUESTION:
Implement a function called 'git_bisect' that takes in a list of commits and a boolean indicating whether the current commit has a bug. The function should return the index of the commit where the bug was introduced, assuming the bug was introduced in one of the commits in the list.
"""

def git_bisect(commits, is_bad_commit):
    """
    This function returns the index of the commit where the bug was introduced.

    Args:
    commits (list): A list of commits.
    is_bad_commit (bool): A boolean indicating whether the current commit has a bug.

    Returns:
    int: The index of the commit where the bug was introduced.
    """
    left, right = 0, len(commits) - 1
    while left < right:
        mid = (left + right) // 2
        # Assuming we have a function that checks if a commit is bad
        if is_bad_commit(commits[mid]):
            right = mid
        else:
            left = mid + 1
    return left