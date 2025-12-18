"""
QUESTION:
Implement a search function called `search_items` that takes two parameters: a list of items and a search query string. The function should return a list of items that match the search query, with the following conditions:
- The function should be case-insensitive.
- The function should support auto-suggest functionality, but for simplicity, it should return all items that contain the search query string.
- The function should support sorting the search results based on multiple criteria.
- The function should support custom filters to refine the search results.
- The function should support pagination for efficient loading of large search result sets.

The input list of items can be assumed to be a list of dictionaries, where each dictionary represents an item with its attributes. The search query string can be any string. The function should return a list of items that match the search query.
"""

def search_items(items, query, sort_by=None, filters=None, page_size=None, page=1):
    """
    Searches a list of items based on a query string and returns the matching items.
    
    Args:
        items (list): A list of dictionaries representing the items to search.
        query (str): The search query string.
        sort_by (str, optional): The attribute to sort the search results by. Defaults to None.
        filters (dict, optional): Custom filters to refine the search results. Defaults to None.
        page_size (int, optional): The number of items to return per page. Defaults to None.
        page (int, optional): The current page number. Defaults to 1.
    
    Returns:
        list: A list of items that match the search query.
    """

    # Convert the query to lowercase for case-insensitive searching
    query = query.lower()

    # Filter the items based on the query string
    search_results = [item for item in items if query in [str(value).lower() for value in item.values()]]

    # Apply custom filters if provided
    if filters:
        search_results = [item for item in search_results if all(item.get(key) == value for key, value in filters.items())]

    # Sort the search results if a sort attribute is provided
    if sort_by:
        search_results = sorted(search_results, key=lambda item: item.get(sort_by))

    # Paginate the search results if a page size is provided
    if page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        search_results = search_results[start_index:end_index]

    return search_results