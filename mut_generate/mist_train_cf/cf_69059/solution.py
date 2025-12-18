"""
QUESTION:
Write a function `calculate_total_folders` that takes in four parameters: `red_folders_boxes`, `red_folders_each_box`, `blue_folders_boxes`, and `blue_folders_each_box`, representing the number of boxes of red folders, the number of folders in each red box, the number of boxes of blue folders, and the number of folders in each blue box, respectively. The function should return the total number of folders. The total number of folders should then be compared to the options 275, 380, 440, and 550, and the nearest option should be determined.
"""

def calculate_total_folders(red_folders_boxes, red_folders_each_box, blue_folders_boxes, blue_folders_each_box):
    """
    Calculate the total number of folders.

    Args:
    red_folders_boxes (int): The number of boxes of red folders.
    red_folders_each_box (int): The number of folders in each red box.
    blue_folders_boxes (int): The number of boxes of blue folders.
    blue_folders_each_box (int): The number of folders in each blue box.

    Returns:
    int: The total number of folders.
    """
    total_red_folders = red_folders_boxes * red_folders_each_box
    total_blue_folders = blue_folders_boxes * blue_folders_each_box
    return total_red_folders + total_blue_folders