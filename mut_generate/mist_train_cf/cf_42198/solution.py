"""
QUESTION:
Implement the function `validate_headers(request)` that takes an HTTP request object and returns `True` if the headers are correctly casted and match the reference dictionary `{b'X-Foo': b'hi'}`, and `False` otherwise. The HTTP request object has a `headers` attribute, which is a dictionary where the keys and values should be bytes. Ensure that the function preserves any bytestrings in the headers.
"""

def validate_headers(request):
    reference_headers = {b'X-Foo': b'hi'}

    for key, value in reference_headers.items():
        if key not in request.headers or request.headers[key] != value:
            return False

    return True