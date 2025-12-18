"""
QUESTION:
Create a function `generate_query` that constructs a query string using two dynamic values. The function should take in two parameters, `value1` and `value2`, and return a string in the following format: "select B,D,G,H where G={value1} and H={value2}". The function should properly concatenate the query string with the dynamic values.
"""

def generate_query(value1, value2):
    """
    This function constructs a query string using two dynamic values.

    Args:
    value1 (str): The first dynamic value for the query string.
    value2 (str): The second dynamic value for the query string.

    Returns:
    str: A query string in the format "select B,D,G,H where G={value1} and H={value2}"
    """
    return f"select B,D,G,H where G={value1} and H={value2}"