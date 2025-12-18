"""
QUESTION:
Write a function called `remove_duplicate_logs` that takes a list of log entries as input, where each log entry is a dictionary containing 'id', 'message', and 'timestamp' fields, and returns a new list containing only the first occurrence of each log entry based on the 'id' field. Assume that the input list is not sorted.
"""

def remove_duplicate_logs(logs):
    """
    Removes duplicate log entries based on the 'id' field.

    Args:
        logs (list): A list of log entries. Each log entry is a dictionary containing 'id', 'message', and 'timestamp' fields.

    Returns:
        list: A new list containing only the first occurrence of each log entry based on the 'id' field.
    """
    seen_ids = set()
    unique_logs = []
    for log in logs:
        if log['id'] not in seen_ids:
            seen_ids.add(log['id'])
            unique_logs.append(log)
    return unique_logs