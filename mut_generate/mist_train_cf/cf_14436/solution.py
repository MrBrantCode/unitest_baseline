"""
QUESTION:
Implement a function `search` that takes two parameters: `text` (the inputted text) and `queries` (a list of search queries). The function should return a dictionary where the keys are the search queries and the values are the number of occurrences of each query in the text. The function should also include suggestions for alternative words or phrases that are similar to each search query.

The search should be case-insensitive and the function should be able to handle multiple search queries. The time complexity of the search algorithm should be less than O(n^2), where n is the length of the inputted text.

Assume that the `text` and `queries` are not empty and the `queries` are comma-separated in a single string.
"""

from difflib import get_close_matches

def search(text, queries):
    """
    Searches for the occurrences of each query in the text and returns a dictionary with the counts and suggestions.

    Args:
        text (str): The inputted text.
        queries (str): Comma-separated search queries.

    Returns:
        dict: A dictionary where the keys are the search queries and the values are dictionaries with the count and suggestions.
    """

    # Convert the text and queries to lower case for case-insensitive search
    text = text.lower()
    queries = [query.strip().lower() for query in queries.split(',')]

    # Process each query
    response = {}
    for query in queries:
        # Count the occurrences of the query in the text
        count = text.count(query)
        response[query] = {'count': count}

        # Get suggestions for alternative words or phrases
        suggestions = get_close_matches(query, text.split(), n=3)
        response[query]['suggestions'] = suggestions

    return response