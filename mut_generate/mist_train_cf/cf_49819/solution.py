"""
QUESTION:
Create a function `paginatedFetch` that handles paginated fetching of data. The function should update `currentPage` and `pageSize` variables based on the "page" and "size" query parameters of the current URL. It should also manage the loading state and error handling. 

The function should handle invalid query parameter values by setting default values when the "page" parameter is less than 1 or the "size" parameter is greater than the maximum allowed page size of 100. The function should not directly manipulate the URL but use provided methods to handle URL changes. 

The function should only be responsible for handling pagination-related data and should not perform any unrelated operations.
"""

def paginatedFetch(pageQuery, sizeQuery, currentPage=1, pageSize=10, maxPageSize=100):
    """
    This function handles paginated fetching of data. It updates currentPage and pageSize variables based on the "page" and "size" query parameters of the current URL.

    Args:
        pageQuery (int): The current page query parameter.
        sizeQuery (int): The current size query parameter.
        currentPage (int, optional): The current page number. Defaults to 1.
        pageSize (int, optional): The current page size. Defaults to 10.
        maxPageSize (int, optional): The maximum allowed page size. Defaults to 100.

    Returns:
        tuple: A tuple containing the updated currentPage and pageSize.
    """
    
    # Check if pageQuery is valid (greater than 0)
    if isinstance(pageQuery, int) and pageQuery > 0:
        currentPage = pageQuery
    
    # Check if sizeQuery is valid (greater than 0 and less than or equal to maxPageSize)
    if isinstance(sizeQuery, int) and sizeQuery > 0 and sizeQuery <= maxPageSize:
        pageSize = sizeQuery
    
    return currentPage, pageSize