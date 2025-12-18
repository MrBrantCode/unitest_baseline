"""
QUESTION:
Create a function called `extract_view_names` that takes a list of URL patterns as input, where each pattern is a string containing a path and a view name enclosed within the 'name=' attribute, separated by a comma. The function should return a dictionary where the keys are the paths and the values are the corresponding view names. The path is enclosed within single quotes and starts after the first opening parenthesis, and the view name is enclosed within single quotes and starts after 'name='. The function should not include any extra characters in the paths and view names.
"""

from typing import List, Dict

def extract_view_names(url_patterns: List[str]) -> Dict[str, str]:
    view_names = {}
    for pattern in url_patterns:
        path_start = pattern.find("(") + 1
        path_end = pattern.find(",", path_start)
        path = pattern[path_start:path_end].strip("'")
        
        view_name_start = pattern.find("name=") + 6
        view_name_end = pattern.find("'", view_name_start)
        view_name = pattern[view_name_start:view_name_end]
        
        view_names[path] = view_name
    
    return view_names