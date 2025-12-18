"""
QUESTION:
Write a function called `aggregate_logs` that takes a dictionary `server_response` as input and returns a dictionary. The input dictionary contains a list of log entries with "timestamp" and "message" keys. The function should aggregate the log entries based on the timestamp and return a dictionary where the keys are timestamps and the values are lists of messages corresponding to that timestamp. The input dictionary has a "logs" key that contains the list of log entries. If the "logs" key does not exist or its value is not a list, consider it as an empty list. If a log entry does not contain "timestamp" or "message" key, skip that entry.
"""

def aggregate_logs(server_response: dict) -> dict:
    logs = server_response.get("logs", [])
    aggregated_logs = {}
    for log in logs:
        timestamp = log.get("timestamp")
        message = log.get("message")
        if timestamp and message:
            aggregated_logs.setdefault(timestamp, []).append(message)
    return aggregated_logs