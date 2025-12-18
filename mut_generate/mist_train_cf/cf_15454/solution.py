"""
QUESTION:
Create a function `createItem` that takes an object with `image` and `caption` properties as an argument. The function should return an HTML element representing a single item with a thumbnail image and a caption. The image should have a width and height of 100 pixels, and the caption should be truncated to 50 characters with an ellipsis if it exceeds this limit. The function should also handle the case where the item is selected and the caption is hovered over. 

The function should be modular, maintainable, and follow best practices such as separation of concerns and reusable components. The output should be compatible with modern browsers and optimized for performance.
"""

def create_item(item):
    """
    Creates an HTML element representing a single item with a thumbnail image and a caption.

    Args:
        item (dict): An object with 'image' and 'caption' properties.

    Returns:
        str: HTML element representing the item.
    """
    image_tag = f"<img src='{item['image']}' width='100' height='100'>"
    caption_tag = f"<div class='caption'>{item['caption'][:47]}...</div>" if len(item['caption']) > 50 else f"<div class='caption'>{item['caption']}</div>"
    return f"<div class='item'>{image_tag}{caption_tag}</div>"