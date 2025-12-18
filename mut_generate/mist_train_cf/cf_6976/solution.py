"""
QUESTION:
Implement a function called `filter_images` that takes in a list of image objects, each containing an image's id, category, and caption, and a filter object containing the filter criteria, including category and search keywords. The function should return a filtered list of image objects that match the specified criteria.
"""

def filter_images(images, filter):
    """
    Filters a list of image objects based on the specified criteria.

    Args:
    images (list): A list of image objects, each containing id, category, and caption.
    filter (dict): A dictionary containing the filter criteria, including category and search keywords.

    Returns:
    list: A filtered list of image objects that match the specified criteria.
    """
    filtered_images = []
    
    # Filter by category
    if 'category' in filter and filter['category']:
        images = [image for image in images if image['category'] == filter['category']]
    
    # Filter by search keywords
    if 'search' in filter and filter['search']:
        search_keywords = filter['search'].lower().split()
        images = [image for image in images if any(keyword in image['caption'].lower() for keyword in search_keywords)]
    
    return images