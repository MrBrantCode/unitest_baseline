"""
QUESTION:
Create a function called `search_keyword` that takes two parameters: `string` and `keyword`. This function should return a list of indices where the `keyword` is found in the `string`, with the search being case-insensitive and allowing for multiple occurrences.
"""

def search_keyword(string, keyword):
    """
    Searches for a keyword in a string and returns a list of indices where the keyword is found.
    
    The search is case-insensitive and allows for multiple occurrences.

    Args:
        string (str): The text to be searched.
        keyword (str): The keyword to search for.

    Returns:
        list: A list of indices where the keyword is found in the string.
    """

    indices = []
    lower_string = string.lower()
    lower_keyword = keyword.lower()
    start_index = lower_string.find(lower_keyword)
    while start_index != -1:
        indices.append(start_index)
        start_index = lower_string.find(lower_keyword, start_index + 1)
    return indices