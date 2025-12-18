"""
QUESTION:
Create a function that generates pagination and sorting metadata for a REST API response. The function should take the following parameters: `total_count`, the total number of items in the result set; `limit`, the maximum number of items per page; `offset`, the current offset in the result set; `sort`, an optional string parameter specifying the sorting criteria; and `order`, an optional string parameter specifying the sorting order. The function should return a dictionary containing the pagination and sorting metadata.
"""

def generate_metadata(total_count, limit, offset, sort=None, order=None):
    """
    Generates pagination and sorting metadata for a REST API response.

    Args:
        total_count (int): The total number of items in the result set.
        limit (int): The maximum number of items per page.
        offset (int): The current offset in the result set.
        sort (str, optional): The sorting criteria. Defaults to None.
        order (str, optional): The sorting order. Defaults to None.

    Returns:
        dict: A dictionary containing the pagination and sorting metadata.
    """

    metadata = {
        "pagination": {
            "total_count": total_count,
            "limit": limit,
            "offset": offset,
            "total_pages": -(-total_count // limit),  # Calculate the ceiling of total_count / limit
        }
    }

    if sort is not None and order is not None:
        metadata["sort"] = {"field": sort, "order": order}

    return metadata