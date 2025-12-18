"""
QUESTION:
Write a function named `git_bisect` that identifies the first bad commit in a sequence of commits using a binary search algorithm. The function should take as input a list of commits and a function that determines whether a commit is good or bad. It should return the index of the first bad commit in the list. The function should assume that the first commit is good and the last commit is bad.
"""

def git_bisect(commits, is_bad_commit):
    """
    Identify the first bad commit in a sequence of commits using a binary search algorithm.

    Args:
    commits (list): A list of commits.
    is_bad_commit (function): A function that determines whether a commit is good or bad.

    Returns:
    int: The index of the first bad commit in the list.
    """
    low, high = 0, len(commits) - 1

    while low < high:
        mid = (low + high) // 2
        if is_bad_commit(commits[mid]):
            high = mid
        else:
            low = mid + 1

    return low