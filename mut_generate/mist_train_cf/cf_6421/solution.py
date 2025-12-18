"""
QUESTION:
Create a function called `merge_branches` that takes two lists of code changes, each representing the modifications made in a separate branch, and returns a merged list that includes all the necessary modifications from each branch. The function should assume that the code changes are represented as strings and should handle conflicts by appending a conflict marker ("CONFLICT") to the merged list when a change is present in both branches.
"""

def merge_branches(branch1, branch2):
    """
    This function merges two lists of code changes from separate branches.
    
    Args:
    branch1 (list): The list of code changes from the first branch.
    branch2 (list): The list of code changes from the second branch.
    
    Returns:
    list: A merged list of code changes, with conflict markers added for changes present in both branches.
    """
    merged_changes = []
    
    # Create a set of changes from the first branch for efficient lookups
    branch1_set = set(branch1)
    
    # Iterate over the changes in the second branch
    for change in branch2:
        # Check if the change is present in the first branch
        if change in branch1_set:
            # If the change is present, add a conflict marker to the merged list
            merged_changes.append("CONFLICT")
        else:
            # If the change is not present, add it to the merged list
            merged_changes.append(change)
    
    # Add the changes from the first branch that are not in the second branch
    for change in branch1:
        if change not in branch2:
            merged_changes.append(change)
    
    return merged_changes