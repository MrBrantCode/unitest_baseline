"""
QUESTION:
Write a function named `search` that takes two parameters: a list of items (documents) and a search string. The function should perform a full text search on the items, returning a list of items that contain the search string. Assume that the items can be serialized to JSON.
"""

def search(items, search_str):
    """
    Performs a full text search on the items and returns a list of items that contain the search string.

    Args:
        items (list): A list of items to search.
        search_str (str): The search string.

    Returns:
        list: A list of items that contain the search string.
    """
    results = []
    for item in items:
        if search_str in json.dumps(item):
            results.append(item)
    return results