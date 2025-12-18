"""
QUESTION:
Implement a function `run` that optimizes the search algorithm for the Johnny Decimal system. The function should take a `JohnnyDecimal` object as input and return the search results filtered by the provided `area`. The `JohnnyDecimal` object contains an `index` representing the Johnny Decimal hierarchy, an `expr` to be searched within the index, and an `area` to filter the search results. The function should efficiently filter the search results based on the provided area using a hierarchical search approach.
"""

class JohnnyDecimal:
    def __init__(self, index, expr, area):
        self.index = index
        self.expr = expr
        self.area = area

def run(johnny_decimal):
    """
    Optimizes the search algorithm for the Johnny Decimal system by filtering search results based on the provided area.

    Args:
        johnny_decimal (JohnnyDecimal): A JohnnyDecimal object containing the index, expression, and area.

    Returns:
        list: A list of search results filtered by the provided area.
    """
    # Initialize an empty list to store the filtered search results
    filtered_results = []

    # Iterate over each item in the index
    for item in johnny_decimal.index:
        # Check if the area of the item matches the provided area
        if item['area'] == johnny_decimal.area:
            # If the areas match, include the item in the search results
            filtered_results.append(item)

    # Return the filtered search results
    return filtered_results