"""
QUESTION:
Implement a `Paginate` class with the following attributes: `start`, `limit`, and `resource`, where `start` is an integer representing the starting index for pagination, `limit` is an integer representing the maximum number of items per page, and `resource` is a list of thread invitation models to be paginated.

The class should have a method `paginate` that calculates the total number of items in the `resource`, determines the subset of thread invitation models to be included in the current page based on the `start` and `limit` parameters, and returns the paginated subset of thread invitation models along with the total number of items. The implementation should handle edge cases such as invalid start and limit values, and should be efficient to handle large datasets without consuming excessive memory.
"""

def paginate(start, limit, resource):
    """
    Paginates the given resource based on the provided start and limit parameters.

    Args:
        start (int): The starting index for pagination.
        limit (int): The maximum number of items per page.
        resource (list): The list of items to be paginated.

    Returns:
        tuple: A tuple containing the paginated subset of items and the total number of items.
    """
    total_items = len(resource)
    if start < 0 or limit <= 0:
        return [], 0  # Return empty list and total count 0 for invalid start or limit

    start_index = min(start, total_items)
    end_index = min(start_index + limit, total_items)

    paginated_items = resource[start_index:end_index]
    return paginated_items, total_items