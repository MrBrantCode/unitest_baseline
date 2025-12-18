"""
QUESTION:
Write a function `transpose_log_groups` that takes a list of log entries as input and returns a list of lists, where each sublist contains log entries between the delimiter "__________". The function should split the log entries into groups based on the delimiter and transpose each group into a list.
"""

def transpose_log_groups(log_entries):
    """
    This function takes a list of log entries, splits them into groups based on the delimiter "__________",
    and transposes each group into a list.

    Args:
        log_entries (list): A list of log entries.

    Returns:
        list: A list of lists, where each sublist contains log entries between the delimiters.
    """

    groups = []
    group = []
    for entry in log_entries:
        if entry == "__________":
            if group:
                groups.append(list(zip(*group)))
                group = []
        else:
            group.append(entry.split())
    if group:
        groups.append(list(zip(*group)))
    return groups