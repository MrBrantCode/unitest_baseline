"""
QUESTION:
Write a function `demarcate_bracket_clusters` that takes a string of clusters of brackets as input, where each cluster is balanced and does not nest inside another. The function should disregard any spaces in the input string and return a list of strings representing the individual bracket clusters.
"""

def demarcate_bracket_clusters(brackets_collection):
    """
    Takes a string of clusters of brackets as input, disregards any spaces, 
    and returns a list of strings representing the individual bracket clusters.

    Args:
        brackets_collection (str): A string of clusters of brackets.

    Returns:
        list: A list of strings representing the individual bracket clusters.
    """
    result = []
    current_cluster = ""
    open_count = 0

    for char in brackets_collection.replace(" ", ""):
        current_cluster += char

        if char == "(":
            open_count += 1
        elif char == ")":
            open_count -= 1

        if open_count == 0 and len(current_cluster) > 0:
            result.append(current_cluster)
            current_cluster = ""

    return result