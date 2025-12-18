"""
QUESTION:
Write a function `application(environ, start_response)` that takes in two parameters: `environ` (a dictionary containing information about the current request and server environment) and `start_response` (a callable that begins the HTTP response). The function should return a string containing the name of the authenticated user if present, or 'Anonymous' otherwise, with a '200 OK' status and 'text/plain' content type.
"""

def application(environ, start_response):
    if 'REMOTE_USER' in environ:
        username = environ['REMOTE_USER']
    else:
        username = 'Anonymous'
    start_response('200 OK', [
        ('Content-Type', 'text/plain')
    ])
    return [f'Hello, {username}']