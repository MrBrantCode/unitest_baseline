"""
QUESTION:
Implement a method `filter_selection_list` for the `ItemProcessor` class. The method should filter the `selectionList` based on the provided `objectLimit` and `selectionQuery`. If `objectLimit` is `None`, all items should be included. If `selectionQuery` is `None`, no filtering based on the query should be performed. The `objectLimit` parameter specifies the maximum number of items to be included in the filtered list, and the `selectionQuery` parameter is a query string used to filter the items in the `selectionList`.
"""

def filter_selection_list(objectLimit, selectionQuery, selectionList):
    """
    Filter the selectionList based on the provided objectLimit and selectionQuery.

    Args:
        objectLimit (int or None): The maximum number of items to be included in the filtered list.
        selectionQuery (str or None): A query string used to filter the items in the selectionList.
        selectionList (list): The list of items to be filtered.

    Returns:
        list: The filtered list of items.
    """
    filtered_list = selectionList

    if selectionQuery:
        filtered_list = [item for item in filtered_list if selectionQuery in item]

    if objectLimit is not None:
        filtered_list = filtered_list[:objectLimit]

    return filtered_list