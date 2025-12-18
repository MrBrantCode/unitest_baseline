"""
QUESTION:
Implement the `clean_string` function, which takes a string or `None` as input and returns a cleaned string. The input string may be up to 1000 characters long. If the input string is `None`, return an empty string. Otherwise, remove all occurrences of "NaN" and any leading/trailing whitespace from the input string.
"""

from typing import Optional

def clean_string(s: Optional[str]) -> str:
    if s is None:
        return ""
    cleaned_str = s.replace("NaN", "").strip()
    return cleaned_str