"""
QUESTION:
Create a function `find_view_function(url_path: str)` that takes a URL path as input and returns the corresponding view function name based on the provided URL patterns. The URL patterns are represented as a list of tuples containing the URL path, the view function, and the view function name. If the URL path matches any pattern, return the name of the corresponding view function; otherwise, return "Not Found". The URL path can be up to 100 characters long and may contain a parameter in the format "<str:name>".
"""

urlpatterns = [
    ('/home/', 'home', 'Home View'),
    ('/about/', 'about', 'About View'),
    ('/contact/<str:name>/', 'contact', 'Contact View'),
]

def find_view_function(url_path: str) -> str:
    for pattern in urlpatterns:
        pattern_path = pattern[0]
        view_function = pattern[1]
        view_name = pattern[2]
        if pattern_path == url_path:
            return view_name
        elif "<str:" in pattern_path:
            pattern_prefix = pattern_path.split("<str:")[0]
            if url_path.startswith(pattern_prefix):
                return view_name
    return "Not Found"