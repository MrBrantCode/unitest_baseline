"""
QUESTION:
Implement a function `search_in_lookup_table` that takes a stream of strings and a target value as input, and returns `True` if the value is found in the stream (ignoring leading and trailing whitespace) and `False` otherwise.
"""

from typing import Iterable

def search_in_lookup_table(lookuptablestream: Iterable[str], value: str) -> bool:
    for table in lookuptablestream:
        if table.strip() == value:
            return True
    return False