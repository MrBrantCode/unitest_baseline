"""
QUESTION:
You were given a string of integer temperature values. Create a function `lowest_temp(t)` and return the lowest value or `None/null/Nothing` if the string is empty.
"""

def lowest_temp(t: str) -> int | None:
    """
    Returns the lowest integer temperature value from a string of space-separated temperature values.
    If the string is empty, returns None.

    :param t: A string of integer temperature values separated by spaces.
    :return: The lowest integer temperature value or None if the string is empty.
    """
    return min((int(x) for x in t.split()), default=None)