"""
QUESTION:
Implement the `render` method in the `ContentServer` class to handle different types of HTTP requests. The method takes a `request` object as a parameter and should return the server's response. The server should respond with the correct content type and data based on the request method. For a `GET` request, the content type should be `text/javascript; charset=UTF-8` and the response should be an empty JSON object. For a `POST` request, the content type should be `application/json; charset=UTF-8` and the response should be a JSON object with a message indicating that the request was received. If the request method is not supported, the response code should be set to 405 (Method Not Allowed) and the response should be an appropriate message.
"""

def render(request):
    if request.method == 'GET':
        request.setHeader('Content-type', 'text/javascript; charset=UTF-8')
        return "{}"
    elif request.method == 'POST':
        request.setHeader('Content-type', 'application/json; charset=UTF-8')
        return '{"message": "Received POST request"}'
    else:
        request.setResponseCode(405)  # Method Not Allowed
        return "Method not allowed for this resource"