"""
QUESTION:
Create a function `extract_view_names` that takes a list of URL patterns as input, where each pattern is a tuple containing a regex pattern and a view name. The function should return a dictionary where the keys are the unique view names and the values are lists of corresponding URL patterns. The function should group duplicate view names together and exclude any duplicate URL patterns for the same view name.
"""

def extract_view_names(url_patterns: list) -> dict:
    view_names_dict = {}
    for pattern, view_name in url_patterns:
        if view_name in view_names_dict:
            if pattern not in view_names_dict[view_name]:
                view_names_dict[view_name].append(pattern)
        else:
            view_names_dict[view_name] = [pattern]
    return view_names_dict