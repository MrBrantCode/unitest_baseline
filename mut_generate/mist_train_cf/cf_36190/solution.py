"""
QUESTION:
Implement the `is_go_view` function, which takes a string `s` as input and returns a boolean value indicating whether the string is a "go view". A "go view" is a string that contains the word "go" and ends with the word "view". The function should perform a case-insensitive comparison.
"""

def is_go_view(s: str) -> bool:
    s = s.lower()  
    return "go" in s and s.endswith("view")