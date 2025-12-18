"""
QUESTION:
Implement a function `processStatusMessage` that takes a status string as input and returns a corresponding message based on the following rules: 
- If the status is "aborted", return "Process aborted by user."
- If the status is "completed", return "Process completed successfully."
- If the status is "pending", return "Process pending, please wait."
- For any other status, return "Invalid status provided."
"""

def processStatusMessage(status):
    if status == "aborted":
        return "Process aborted by user."
    elif status == "completed":
        return "Process completed successfully."
    elif status == "pending":
        return "Process pending, please wait."
    else:
        return "Invalid status provided."