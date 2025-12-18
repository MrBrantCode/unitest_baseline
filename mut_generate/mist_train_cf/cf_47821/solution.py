"""
QUESTION:
Create a function called `calculate_fill_factor` that determines a suitable fill factor for a database table based on the given parameters. The function should take four parameters: `read_frequency`, `write_frequency`, `fragmentation_level`, and `maintenance_window`, and return a fill factor value between 0 and 100. The function should consider the pattern of database usage, index fragmentation, server performance, and maintenance window when calculating the fill factor.
"""

def calculate_fill_factor(read_frequency, write_frequency, fragmentation_level, maintenance_window):
    """
    Calculate a suitable fill factor for a database table based on the given parameters.

    Args:
        read_frequency (float): The frequency of read operations.
        write_frequency (float): The frequency of write operations.
        fragmentation_level (float): The level of index fragmentation.
        maintenance_window (float): The maintenance window.

    Returns:
        int: A fill factor value between 0 and 100.
    """

    # Pattern of Database Usage
    if read_frequency > write_frequency:
        # Data is mostly read and rarely changes
        fill_factor = 90
    else:
        # There's a mix of reading and writing the data
        fill_factor = 70

    # Index fragmentation
    if fragmentation_level > 50:
        # Higher fragmentation means a lower fill factor
        fill_factor -= 10

    # Server Performance
    # This factor is not directly quantifiable, consider it as a constant adjustment
    # If queries are mainly read and server I/O isn't a problem, consider a high fill factor
    if read_frequency > 0.8:
        fill_factor += 5

    # Maintenance Window
    if maintenance_window < 1:
        # Short window for maintenance, consider a higher fill factor
        fill_factor += 5

    # Ensure the fill factor is within the valid range
    fill_factor = max(0, min(fill_factor, 100))

    return fill_factor