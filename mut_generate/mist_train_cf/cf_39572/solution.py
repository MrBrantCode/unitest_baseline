"""
QUESTION:
Create a function `process_query(query)` that takes a string `query` as input, ignores case sensitivity and punctuation, and returns a dictionary containing the frequency of each word in the query. The function should consider only alphanumeric characters as part of a word. The input query can contain any printable ASCII characters.
"""

import re
from collections import Counter

def process_query(query: str) -> dict:
    query = re.sub(r'[^\w\s]', '', query).lower()
    return dict(Counter(query.split()))