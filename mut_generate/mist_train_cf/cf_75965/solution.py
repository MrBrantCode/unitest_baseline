"""
QUESTION:
Design a function called `create_http_header` that constructs a custom HTTP header for a POST request. The function should have error handling capabilities to prevent crashes in cases of faulty inputs. The function should take in three parameters: `content_type` (with a default value of "application/json"), `accept` (with a default value of "application/json"), and `other_header` (with a default value of an empty dictionary). The function should return a dictionary containing the HTTP headers.
"""

def create_http_header(content_type="application/json", accept="application/json", other_header={}):
    headers = {
        "Content-Type": content_type,
        "Accept": accept
    }
    headers.update(other_header)
    return headers