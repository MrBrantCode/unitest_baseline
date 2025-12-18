"""
QUESTION:
Create a function `handle_http_request(request_method)` that takes a string `request_method` representing an HTTP request method and returns a message based on the request method. The function should return the following messages for the corresponding request methods:
- 'POST': "Received a POST request."
- 'GET': "Received a GET request."
- 'HEAD': "Received a HEAD request."
- Any other request method: "Invalid request method."
"""

def handle_http_request(request_method):
    if request_method == 'POST':
        return "Received a POST request."
    elif request_method == 'GET':
        return "Received a GET request."
    elif request_method == 'HEAD':
        return "Received a HEAD request."
    else:
        return "Invalid request method."