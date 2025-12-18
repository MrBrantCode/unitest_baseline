"""
QUESTION:
Create a function called `paginate_results` that takes in a list of search results and a page number, and returns the paginated results for the specified page. The function should assume a fixed page size of 20 results per page. 

The input list of search results can be of any length, and the page number should be a positive integer. If the page number is out of range, the function should return an empty list. The function should not perform any error checking on the inputs.
"""

def paginate_results(search_results, page):
    """
    This function takes in a list of search results and a page number, 
    and returns the paginated results for the specified page.
    
    Args:
        search_results (list): A list of search results.
        page (int): The page number.
    
    Returns:
        list: The paginated results for the specified page.
    """
    page_size = 20  # Fixed page size of 20 results per page
    start_index = (page - 1) * page_size
    end_index = page * page_size
    
    # Return an empty list if the page number is out of range
    if start_index >= len(search_results):
        return []
    
    # Return the paginated results for the specified page
    return search_results[start_index:end_index]