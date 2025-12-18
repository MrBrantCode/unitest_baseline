"""
QUESTION:
Implement a function `getPaginatedItems` to display a list of items from a local database with pagination and user filtering capabilities, following the Model-View-ViewModel (MVVM) architectural pattern. The function should accept a `limit` parameter to control the number of items per page and a `filter` parameter to filter items based on user input. The function should return a list of items for the current page.
"""

def getPaginatedItems(limit, filter, items, page_number):
    """
    Returns a list of items for the current page with pagination and filtering capabilities.

    Args:
    limit (int): The number of items per page.
    filter (str): The filter string to filter items.
    items (list): The list of all items.
    page_number (int): The current page number.

    Returns:
    list: A list of items for the current page.
    """
    # Filter items based on the filter string
    filtered_items = [item for item in items if filter.lower() in str(item).lower()]
    
    # Calculate the start and end indices for the current page
    start_index = (page_number - 1) * limit
    end_index = start_index + limit
    
    # Return the items for the current page
    return filtered_items[start_index:end_index]