"""
QUESTION:
Implement a function called `find_closest_matches` that takes two lists of strings as input, representing titles from two different news feeds, and returns a dictionary where the keys are the titles from the first feed and the values are the closest matching titles from the second feed.

The function should use the `difflib.get_close_matches` function with a cutoff of 0.01 to find the closest matching title for each title in the first feed. If no match is found for a title, the value in the output dictionary should be `None`.

Input:
- `cnn_titles` (List[str]): A list of titles from the first news feed.
- `cbc_titles` (List[str]): A list of titles from the second news feed.

Output:
- A dictionary where the keys are the titles from the first feed and the values are the closest matching titles from the second feed.
"""

from typing import List, Dict
import difflib

def find_closest_matches(cnn_titles: List[str], cbc_titles: List[str]) -> Dict[str, str]:
    closest_matches = {}
    for title in cnn_titles:
        match = difflib.get_close_matches(title, cbc_titles, 1, 0.01)
        closest_matches[title] = match[0] if match else None
    return closest_matches