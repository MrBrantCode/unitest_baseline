"""
QUESTION:
Design a function named 'artwork_filter' that filters artworks based on given parameters. The function should take as input a list of artwork objects and a dictionary of filter parameters. The artwork object should have the following attributes: 'title', 'tags', and 'copyright'. The filter parameters dictionary should have the following keys: 'title', 'tags', and 'copyright'. If a key is present in the filter parameters dictionary, the function should only return artworks that match the corresponding value. If a key is not present in the filter parameters dictionary, the function should not filter based on that attribute.
"""

def artwork_filter(artworks, filter_params):
    """
    Filters artworks based on given parameters.

    Args:
        artworks (list): A list of artwork objects.
        filter_params (dict): A dictionary of filter parameters.

    Returns:
        list: A list of filtered artwork objects.
    """
    filtered_artworks = artworks.copy()

    if 'title' in filter_params:
        filtered_artworks = [artwork for artwork in filtered_artworks if artwork.title == filter_params['title']]

    if 'tags' in filter_params:
        filtered_artworks = [artwork for artwork in filtered_artworks if set(filter_params['tags']).issubset(set(artwork.tags))]

    if 'copyright' in filter_params:
        filtered_artworks = [artwork for artwork in filtered_artworks if artwork.copyright == filter_params['copyright']]

    return filtered_artworks