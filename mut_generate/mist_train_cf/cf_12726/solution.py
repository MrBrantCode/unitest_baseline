"""
QUESTION:
Design a function `create_search_bar` that structures a web page with a search bar supporting autocomplete functionality and dynamic search result updates. The function should implement the following restrictions: 
- the search results should be clickable
- the search results should be dynamically updated as the user types, without reloading the page
- the search bar should suggest search terms as the user types
"""

def create_search_bar(query, search_data):
    """
    Structures a web page with a search bar supporting autocomplete functionality 
    and dynamic search result updates.

    Args:
    query (str): The user's search query.
    search_data (list): A list of possible search results.

    Returns:
    list: A list of search results based on the query.
    """

    # Initialize an empty list to store search results
    search_results = []

    # Iterate over each item in the search data
    for item in search_data:
        # Check if the query is present in the item
        if query.lower() in item.lower():
            # If the query is present, add the item to the search results
            search_results.append(item)

    # Return the search results
    return search_results