"""
QUESTION:
Create a function `get_num_samples` that takes a list of rows as input, where each row is an object with `sample_label` and `num_samples` attributes. The function should return the `num_samples` value from the row where `sample_label` equals 0. If no such row exists, the function should return `None`.
"""

def get_num_samples(rows):
    """
    Returns the num_samples value from the row where sample_label equals 0.
    If no such row exists, returns None.

    Args:
        rows (list): A list of rows where each row is an object with sample_label and num_samples attributes.

    Returns:
        int or None: The num_samples value or None if not found.
    """
    for row in rows:
        if row.sample_label == 0:
            return row.num_samples
    return None