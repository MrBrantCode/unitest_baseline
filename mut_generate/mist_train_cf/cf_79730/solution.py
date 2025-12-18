"""
QUESTION:
Create a function named `git_bisect` to simulate the 'git bisect' command in identifying the precise commit that triggered a software glitch. The function should take in two parameters: `commits`, a list of boolean values where `True` represents a bad commit and `False` represents a good commit, and `bad_commit`, the index of the bad commit in the `commits` list. The function should return the index of the bad commit. The `git_bisect` function should use a binary search approach to find the bad commit.
"""

def git_bisect(commits, bad_commit):
    """
    Simulates the 'git bisect' command to identify the precise commit that triggered a software glitch.

    Args:
    commits (list): A list of boolean values where True represents a bad commit and False represents a good commit.
    bad_commit (int): The index of the bad commit in the commits list.

    Returns:
    int: The index of the bad commit.
    """
    left, right = 0, len(commits) - 1
    while left < right:
        mid = (left + right) // 2
        if commits[mid]:
            right = mid
        else:
            left = mid + 1
    return left