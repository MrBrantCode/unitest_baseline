"""
QUESTION:
Write a function named `interpret_status_code` that takes a response object from a PATCH request as input and categorizes its status code into four groups: success (200-299), redirection (300-399), client error (400-499), and server error (500 and above). The function should handle cases where the input response is None, indicating a failed request.
"""

def interpret_status_code(response):
    """
    Categorizes the status code of a response object from a PATCH request.

    Args:
        response: A response object from a PATCH request.

    Returns:
        A string describing the status code category.
    """
    if response is None:
        return "Request failed"
    elif response.status_code >= 200 and response.status_code < 300:
        return "Success"
    elif response.status_code >= 300 and response.status_code < 400:
        return "Redirection"
    elif response.status_code >= 400 and response.status_code < 500:
        return "Client Error"
    elif response.status_code >= 500:
        return "Server Error"