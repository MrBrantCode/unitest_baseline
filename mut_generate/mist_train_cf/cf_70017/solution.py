"""
QUESTION:
Rename all .jpg files to .jpeg in a database column. Write a function to update a database table column to replace all instances of '.jpg' with '.jpeg' if the column value contains '.jpg'.
"""

def replace_jpg_with_jpeg(column_value):
    """
    Replaces all instances of '.jpg' with '.jpeg' in a given column value.

    Args:
    column_value (str): The value of the column to be updated.

    Returns:
    str: The updated column value with '.jpg' replaced by '.jpeg'.
    """
    return column_value.replace('.jpg', '.jpeg')