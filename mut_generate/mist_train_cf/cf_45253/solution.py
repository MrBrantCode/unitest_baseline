"""
QUESTION:
Create a function `sync_etsy_instagram` that synchronizes item lists between Etsy and Instagram Shop. The function should replicate any changes (addition, edit, deletion) to items on one platform to the other. Additionally, it should also sync sales data between the two platforms.
"""

def sync_etsy_instagram(etsy_items, instagram_items):
    """
    Synchronizes item lists between Etsy and Instagram Shop.

    Args:
        etsy_items (list): List of items on Etsy.
        instagram_items (list): List of items on Instagram Shop.

    Returns:
        tuple: A tuple containing the updated lists of items on Etsy and Instagram Shop.
    """

    # Sync addition and edits
    for etsy_item in etsy_items:
        if etsy_item not in instagram_items:
            instagram_items.append(etsy_item)

    for instagram_item in instagram_items:
        if instagram_item not in etsy_items:
            etsy_items.append(instagram_item)

    # Sync deletion
    etsy_items = [item for item in etsy_items if item in instagram_items]
    instagram_items = [item for item in instagram_items if item in etsy_items]

    # Sync sales data (assuming sales data is a part of each item)
    for etsy_item in etsy_items:
        for instagram_item in instagram_items:
            if etsy_item['id'] == instagram_item['id']:
                instagram_item['sales'] = etsy_item['sales']

    return etsy_items, instagram_items