"""
QUESTION:
Write a function `get_error_message(error_code: int) -> str` that takes an integer error code as input and returns its corresponding error message. The error codes are structured as a 5-digit number where the first digit represents the error type, the next two digits represent the error category, and the last two digits represent the specific error. If the error code is not found, return "Error code not found".
"""

def get_error_message(error_code: int) -> str:
    error_messages = {
        31522: 'Positive keyword not loaded (UniquenessError)',
        31531: 'Negative keyword not loaded (TypeError)',
        31532: 'Negative keyword not loaded (UniquenessError)',
        40000: 'Unknown error'
    }
    
    return error_messages.get(error_code, "Error code not found")