"""
QUESTION:
Write a function `processLogSnippet` that takes a log file snippet as input and returns a dictionary containing the error message and the flag status. The function should extract the error message represented by the `DZError` function and the flag status represented by the `Abort_Flag` and `Fatal` function, ignoring commented out code. The dictionary should include the error message with the key "error_message" and its value, and the flag status with the key "flag_status" and its value (either "set" or "not set").
"""

import re

def processLogSnippet(logSnippet):
    result = {"error_message": None, "flag_status": None}

    # Extract error message
    error_match = re.search(r'DZError\((.*?)\)', logSnippet)
    if error_match:
        result["error_message"] = error_match.group()

    # Extract flag status
    flag_match = re.search(r'if\s*\((.*?)\)', logSnippet)
    if flag_match:
        flag_status = "set" if "Abort_Flag" in flag_match.group() else "not set"
        result["flag_status"] = flag_status

    return result