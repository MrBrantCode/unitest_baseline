"""
QUESTION:
Create a function called `extract_metadata` that takes a list of strings `metadata` as input and returns a tuple containing the programming language and a list of keywords. The programming language should be extracted from the string that starts with "Programming Language ::" and the keywords should be extracted from the string containing 'keywords'. 

The function should handle cases where the required information is not present in the metadata, returning `None` for the programming language and an empty list for the keywords in such cases.
"""

from typing import List, Tuple

def extract_metadata(metadata: List[str]) -> Tuple[str, List[str]]:
    programming_language = next((data.split('::')[1].strip() for data in metadata if data.startswith('Programming Language ::')), None)
    keywords = next((eval(data.split('=')[1].strip()) for data in metadata if 'keywords' in data), [])

    return programming_language, keywords