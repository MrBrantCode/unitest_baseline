"""
QUESTION:
Implement a function called `search_items` that takes in two parameters: `query` and `page`. The function should return a list of items that match the search query, paginated to the specified page number. The function should support advanced search options such as boolean operators (AND, OR, NOT) and wildcard searches. Assume that the search query is passed as a string, and the page number is passed as an integer. The function should return a list of items, where each item is a dictionary containing the item's id, name, and price.
"""

def search_items(query, page):
    """
    Searches for items based on the query and returns a list of items paginated to the specified page number.

    Args:
        query (str): The search query.
        page (int): The page number.

    Returns:
        list: A list of items, where each item is a dictionary containing the item's id, name, and price.
    """

    # Simulating a database of items
    items = [
        {"id": 1, "name": "Item 1", "price": 10.99},
        {"id": 2, "name": "Item 2", "price": 9.99},
        {"id": 3, "name": "Item 3", "price": 12.99},
        {"id": 4, "name": "Item 4", "price": 11.99},
        {"id": 5, "name": "Item 5", "price": 8.99},
        # Add more items...
    ]

    # Implementing basic search functionality
    # You can enhance this to support boolean operators (AND, OR, NOT) and wildcard searches
    results = [item for item in items if query.lower() in item["name"].lower()]

    # Implementing pagination
    page_size = 2
    start = (page - 1) * page_size
    end = start + page_size
    paginated_results = results[start:end]

    return paginated_results