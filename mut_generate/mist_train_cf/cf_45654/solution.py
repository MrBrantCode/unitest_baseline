"""
QUESTION:
Create a function called `facebook_link_post` to share a link on Facebook without displaying the link title and description, and display the link image in a large size. Note that the function should take into account Facebook's metadata requirements and limitations on removing link title and description. The function should also ensure the image size meets Facebook's recommended ratio of 1.91:1 for optimal display.
"""

def update_metadata(url, title, description, image_url, image_ratio):
    """
    Simulate updating a webpage's metadata.

    Args:
        url (str): The URL of the webpage.
        title (str): The new title of the webpage.
        description (str): The new description of the webpage.
        image_url (str): The URL of the image.
        image_ratio (float): The aspect ratio of the image.

    Returns:
        dict: A dictionary representing the updated metadata.
    """

    # Simulate updating the webpage's metadata
    metadata = {
        'url': url,
        'title': title,
        'description': description,
        'image_url': image_url,
        'image_ratio': image_ratio
    }

    # Check if the image ratio meets Facebook's recommended ratio
    if image_ratio != 1.91:
        print("Note: The image ratio does not meet Facebook's recommended ratio of 1.91:1.")

    return metadata