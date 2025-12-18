"""
QUESTION:
Create a function `git_bisect` that simulates the Git bisect command. It should take as input a list of commits and a function `is_bad` that checks whether a commit is bad or not. The function should return the first bad commit in the list, or None if no bad commit is found.

The function should implement a binary search algorithm on the list of commits and use the `is_bad` function to determine whether each commit is bad or not. The function should also handle the case where the input list is empty or where there are no bad commits in the list.

Note that this function is a simulation of the Git bisect command and does not actually interact with the Git version control system.
"""

def git_bisect(commits, is_bad):
    """
    Simulates the Git bisect command by implementing a binary search algorithm on the list of commits.
    
    Args:
        commits (list): A list of commits.
        is_bad (function): A function that checks whether a commit is bad or not.
    
    Returns:
        The first bad commit in the list, or None if no bad commit is found.
    """

    # Handle the edge case where the input list is empty
    if not commits:
        return None

    # Initialize two pointers, one at the start and one at the end of the list
    left, right = 0, len(commits) - 1

    # Continue the binary search until the two pointers meet
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # Check if the commit at the middle index is bad
        if is_bad(commits[mid]):
            # If the middle commit is bad, check if it's the first bad commit
            if mid == 0 or not is_bad(commits[mid - 1]):
                return commits[mid]
            # If not, move the right pointer to the left of the middle index
            else:
                right = mid - 1
        else:
            # If the middle commit is not bad, move the left pointer to the right of the middle index
            left = mid + 1

    # If no bad commit is found, return None
    return None