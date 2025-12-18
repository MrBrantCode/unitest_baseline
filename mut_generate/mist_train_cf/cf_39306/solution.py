"""
QUESTION:
Create a function named `get_http_status_message` that takes an integer HTTP status code as input and returns its corresponding HTTP status message. The function should handle standard HTTP status codes and the custom status code 418. If the input status code does not have a corresponding message, the function should return 'Unknown Status Code'.
"""

def entrance(status_code: int) -> str:
    http_status_messages = {
        200: 'OK',
        201: 'Created',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        413: 'Request Entity Too Large',
        414: 'Request URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Requested Range Not Satisfiable',
        417: 'Expectation Failed',
        418: "I'm a teapot",
        428: 'Precondition Required',
        429: 'Too Many Requests',
        431: 'Request Header Fields Too Large',
        500: 'Internal Server Error',
        501: 'Not Implemented'
    }

    return http_status_messages.get(status_code, 'Unknown Status Code')