"""
QUESTION:
Write a function `convertFileSize` that takes a string `size` representing the size of a file in bytes as input. The function should convert this size into a human-readable format by converting it into the most appropriate unit (bytes, kilobytes, megabytes, gigabytes, etc.) and round the result to two decimal places. The input size is a string of digits, and the function should return a string containing the converted size and unit (e.g., "976.56 KB").
"""

def convertFileSize(size: str) -> str:
    """
    Converts a file size in bytes to a human-readable format.

    Args:
    size (str): The size of the file in bytes.

    Returns:
    str: The file size in a human-readable format (e.g., "976.56 KB").
    """

    # Convert the input size to an integer
    size = int(size)

    # Define the units for the file size
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    # Initialize the unit index to 0 (bytes)
    unit_index = 0

    # Convert the size to the most appropriate unit
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    # Return the converted size and unit, rounded to two decimal places
    return f"{size:.2f} {units[unit_index]}"