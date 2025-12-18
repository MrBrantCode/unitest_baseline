"""
QUESTION:
Implement a function `updateData` that takes no parameters and updates the `display_data` structure by incrementing its `historical` sub-structure's `ppm_length` by 1 and resetting `span_average_count` to 0.
"""

def updateData(display_data):
    """
    Updates the display_data structure by incrementing its historical sub-structure's ppm_length by 1 
    and resetting span_average_count to 0.

    Args:
        display_data (dict): The data structure to be updated.

    Returns:
        dict: The updated display_data structure.
    """
    display_data['historical']['ppm_length'] += 1
    display_data['historical']['span_average_count'] = 0  # Assuming span_average_count is within historical
    return display_data