"""
QUESTION:
Create a function `check_for_no` that takes a list of elements as input and returns a boolean value. The function should iterate through the list and return True if any string element contains the word 'No', and False otherwise. If a non-string element is encountered during iteration, an exception should be handled and the function should return False.
"""

from typing import List

def check_for_no(strings: List[str]) -> bool:
    try:
        for s in strings:
            if 'No' in str(s):
                return True
    except Exception:
        pass
    return False