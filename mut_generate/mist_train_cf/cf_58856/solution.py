"""
QUESTION:
Write a function called `merge_branches` that determines if it's possible to merge two branches in a version control system given their common ancestor. The function should take two parameters: `ancestor` and `branch1` and `branch2`, which are the commit hashes of the common ancestor and the two branches respectively. The function should return a boolean indicating whether a merge is possible. 

Restrictions: Assume that the version control system is similar to TFS and that the branches have a common ancestor.
"""

def merge_branches(ancestor, branch1, branch2):
    # In a real implementation, you'd have a graph of commits and check if branch1 and branch2 have a common ancestor
    # For simplicity, this example assumes that the ancestor is indeed common to both branches
    return True