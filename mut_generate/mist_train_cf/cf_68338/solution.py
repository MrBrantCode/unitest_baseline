"""
QUESTION:
Implement a function `optimize_artwork_archive` that optimizes the digital artwork archive platform for optimal responsiveness and minimal loading times. The function should ensure the platform includes advanced search options, user ratings, and sorting functionalities.
"""

def optimize_artwork_archive(artworks, search_query=None, sort_by=None):
    """
    Optimizes the digital artwork archive platform by applying search filters and sorting options.

    Args:
        artworks (list): A list of dictionaries containing artwork metadata.
        search_query (str): The search query to filter artworks by.
        sort_by (str): The field to sort artworks by.

    Returns:
        list: The filtered and sorted list of artworks.
    """

    # Filter artworks by search query if provided
    if search_query:
        artworks = [artwork for artwork in artworks if search_query.lower() in artwork['title'].lower() or search_query.lower() in artwork['artist'].lower()]

    # Sort artworks by the specified field if provided
    if sort_by:
        artworks.sort(key=lambda artwork: artwork.get(sort_by, ''))

    return artworks