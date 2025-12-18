"""
QUESTION:
You are tasked with creating a function that maps URL paths to their corresponding view function names in a Django application. The function, named `find_view_function`, takes a URL path as input and returns the associated view function name if the path matches any of the defined patterns, otherwise it returns "Not Found". The function should only consider exact matches from the start of the URL path.

Function Signature: `def find_view_function(url_path: str) -> str`
"""

def find_view_function(url_path: str) -> str:
    url_patterns = {
        '': 'icecream_list',
        '<int:pk>/': 'icecream_detail',
        '<str:username>/unfollow/': 'profile_unfollow',
        '<str:username>/follow/': 'profile_follow',
        '<str:username>/': 'profile',
        '<str:pk>/unfav/': 'favourite_unfollow',
        '<str:pk>/fav/': 'favourite_follow',
    }

    for pattern, view_function in url_patterns.items():
        if url_path == pattern:
            return view_function

    return "Not Found"