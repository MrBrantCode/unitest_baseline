"""
QUESTION:
Implement the `search_images` function in Python. It should allow users to search for images based on their titles, descriptions, or tags, and have a time complexity of O(log n) or better. The function should take in a list of images and a search query as input, and return a list of images that match the search query. Each image should be represented as a dictionary with 'title', 'description', and 'tags' keys.
"""

def search_images(images, query):
    """
    Searches for images based on their titles, descriptions, or tags.

    Args:
        images (list): A list of dictionaries representing images with 'title', 'description', and 'tags' keys.
        query (str): The search query.

    Returns:
        list: A list of images that match the search query.
    """
    query = query.lower()
    return [image for image in images if query in image['title'].lower() or query in image['description'].lower() or query in [tag.lower() for tag in image['tags']]]