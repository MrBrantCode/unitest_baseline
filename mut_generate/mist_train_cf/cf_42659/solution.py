"""
QUESTION:
Write a function `parseRoutes` that takes a string `code_snippet` as input and returns a dictionary where the keys are the route paths and the values are the corresponding controller methods. The function should ignore commented lines (starting with `//`) and extract the route paths and controller methods from the uncommented lines starting with `Route::get`.
"""

import re

def parseRoutes(code_snippet):
    routes = {}
    lines = code_snippet.split('\n')
    for line in lines:
        if line.strip().startswith('Route::get') and not line.strip().startswith('//'):
            route_path = re.search(r"'(.*?)'", line).group(1)
            controller_method = re.search(r"\[.*'(.*)'\]", line).group(1)
            routes[route_path] = controller_method
    return routes