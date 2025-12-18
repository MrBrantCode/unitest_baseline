"""
QUESTION:
Implement a 'what_if_analysis' function that performs a scenario analysis on a given OLAP cube. The function should take in the OLAP cube and a list of changes as input, where each change is represented as a dictionary containing the dimension name, the old hierarchy, and the new hierarchy. The function should return the modified OLAP cube after applying the changes.

Restrictions: The input OLAP cube is a multi-dimensional array, and the changes should be applied to the hierarchies of the dimensions.
"""

def what_if_analysis(cube, changes):
    """
    Performs a scenario analysis on a given OLAP cube by applying a list of changes.

    Args:
    - cube (multi-dimensional array): The input OLAP cube.
    - changes (list of dictionaries): A list of changes, where each change contains the dimension name, old hierarchy, and new hierarchy.

    Returns:
    - The modified OLAP cube after applying the changes.
    """
    
    # Create a copy of the OLAP cube to avoid modifying the original data
    modified_cube = [row[:] for row in cube]

    # Apply the changes to the hierarchies of the dimensions
    for change in changes:
        dimension = change['dimension']
        old_hierarchy = change['old_hierarchy']
        new_hierarchy = change['new_hierarchy']

        # Replace the old hierarchy with the new hierarchy in the modified cube
        for i, row in enumerate(modified_cube):
            if row[dimension] == old_hierarchy:
                modified_cube[i][dimension] = new_hierarchy

    return modified_cube