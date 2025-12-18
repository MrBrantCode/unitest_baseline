"""
QUESTION:
Implement a function named `shared_view_contexts` that takes a list of HTTP request objects as input, where each request object is a dictionary with keys representing context variables and their corresponding values. The function should return a dictionary containing the shared view contexts present in all the requests, which are the context variables that are present in all the requests with the same values. The function must work efficiently and handle an empty list of requests by returning an empty dictionary.
"""

from typing import List, Dict, Any

def shared_view_contexts(requests: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not requests:
        return {}

    shared_contexts = {}
    for key in requests[0].keys():
        values = set(request.get(key) for request in requests)
        if len(values) == 1:
            shared_contexts[key] = requests[0][key]

    return shared_contexts