"""
QUESTION:
Create a function called `extract_view_names` that takes a list of URL paths as input and returns a dictionary of view names and their corresponding paths. The view name is the part of the URL path that comes after the last forward slash ("/") and before any query parameters or file extensions. The function should handle URL paths that may contain query parameters or file extensions, and it should use the last occurrence of each view name as its value in the returned dictionary.
"""

from typing import List, Dict

def extract_view_names(url_paths: List[str]) -> Dict[str, str]:
    view_names = {}
    for path in url_paths:
        parts = path.rstrip("/").split("/")
        view_name = parts[-1]
        if "?" in view_name:
            view_name = view_name[:view_name.index("?")]
        if "." in view_name:
            view_name = view_name[:view_name.index(".")]
        view_names[view_name] = path
    return view_names