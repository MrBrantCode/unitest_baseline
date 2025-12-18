"""
QUESTION:
Design a function `get_error_message` that takes a file-related error code as input and returns a corresponding error message. The error code can be one of the following: `FMOD_ERR_FILE_COULDNOTSEEK`, `FMOD_ERR_FILE_DISKEJECTED`, `FMOD_ERR_FILE_EOF`, `FMOD_ERR_FILE_ENDOFDATA`, or `FMOD_ERR_FILE_NOTFOUND`. The function should return a meaningful error message for each scenario. If the error code is not recognized, the function should return a generic "Unknown file-related error" message.
"""

def get_error_message(error_code):
    """
    Returns a meaningful error message for a given file-related error code.

    Args:
        error_code (str): A file-related error code.

    Returns:
        str: A corresponding error message for the given error code.
    """
    error_messages = {
        "FMOD_ERR_FILE_COULDNOTSEEK": "Media file could not be seeked.",
        "FMOD_ERR_FILE_DISKEJECTED": "Media was ejected while reading.",
        "FMOD_ERR_FILE_EOF": "End of file unexpectedly reached while trying to read essential data (truncated?).",
        "FMOD_ERR_FILE_ENDOFDATA": "End of current chunk reached while trying to read data.",
        "FMOD_ERR_FILE_NOTFOUND": "File not found."
    }

    return error_messages.get(error_code, "Unknown file-related error.")