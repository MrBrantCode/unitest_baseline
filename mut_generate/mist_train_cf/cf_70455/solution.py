"""
QUESTION:
Design a function named `google_search(search_term, time_window)` that generates a Google search URL based on the given search term and time window. The search term can be any phrase or term, and the time window can be one of the following: 'past hour', 'past 24 hours', 'past week', 'past month', or 'past year'. The time window should be filtered using Google's 'tbs' query parameter, where 'past hour' maps to 'qdr:h', 'past 24 hours' maps to 'qdr:d', 'past week' maps to 'qdr:w', 'past month' maps to 'qdr:m', and 'past year' maps to 'qdr:y'.
"""

import urllib.parse

def google_search(search_term, time_window):
    time_window_codes = {
        "past hour": "qdr:h",
        "past 24 hours": "qdr:d",
        "past week": "qdr:w",
        "past month": "qdr:m",
        "past year": "qdr:y"
    }
    
    base_url = "https://www.google.com/search"
    query_param = urllib.parse.urlencode({'q': search_term, 'tbs': time_window_codes[time_window]})
    total_url = base_url + "?" + query_param
    return total_url