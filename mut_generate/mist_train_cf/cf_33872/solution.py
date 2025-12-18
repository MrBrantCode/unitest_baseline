"""
QUESTION:
Implement a function `generate_modified_requests(payloads, body, param_name, methods, url, headers, source)` that generates a list of modified HTTP requests based on different sources of input data. The function takes in the following parameters:

* `payloads`: A list of payloads to be used for modification.
* `body`: The original request body.
* `param_name`: The name of the parameter to be modified.
* `methods`: A list of HTTP methods to be used for the requests.
* `url`: The URL of the web application.
* `headers`: The original request headers.
* `source`: The source of input data, which can be either "POST" or "COOKIE".

The function should return a list of modified HTTP requests. The `asp_post_hpp` function should modify the request body based on the payload and param_name, and the `asp_cookie_hpp` function should modify the request headers based on the payload and param_name.
"""

def generate_modified_requests(payloads, body, param_name, methods, url, headers, source):
    requests = []
    if source.upper() == "POST":
        for payload in payloads:
            new_body = body.replace(param_name, payload)
            for method in methods:
                requests.append({"method": method, "url": url, "body": new_body, "headers": headers})
    elif source.upper() == "COOKIE":
        for payload in payloads:
            new_headers = headers.copy()
            new_headers[param_name] = payload
            for method in methods:
                requests.append({"method": method, "url": url, "body": body, "headers": new_headers})
    return requests