"""
QUESTION:
Implement a function named `supports_xhtml` that takes a `request` object as input and returns a boolean value indicating whether the client's browser supports XHTML. The function should analyze the `request` object, specifically its `headers` attribute, to determine XHTML support based on the user-agent string or other relevant information. The `request` object is assumed to have the necessary attributes to determine XHTML support.
"""

def supports_xhtml(request):
    user_agent = request.headers.get('User-Agent', '')
    return 'XHTML' in user_agent