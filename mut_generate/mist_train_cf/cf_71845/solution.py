"""
QUESTION:
Write a function named `hello_world` that represents an HTTP Cloud Function. The function takes a Flask request object as input and returns a response text. The response should be the 'message' from either the request arguments or the request JSON, or 'Hello, World!' if no 'message' is found. The function should be deployable on Google Cloud Functions using the Python runtime.
"""

def hello_world(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello, World!'