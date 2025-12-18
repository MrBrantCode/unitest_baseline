"""
QUESTION:
Write a function `clean_search_term` that takes a string `search_term` and a list of strings `stop_words` as input and returns a string where all occurrences of `stop_words` in `search_term` are removed. The function should perform a case-insensitive search for `stop_words` and consider whole words only.
"""

from typing import List
import re

def clean_search_term(search_term: str, stop_words: List[str]) -> str:
    stop_word_list = re.compile(r'\b(?:' + '|'.join(stop_words) + r')\b', re.IGNORECASE)
    cleaned_search_term = stop_word_list.sub('', search_term)
    return cleaned_search_term