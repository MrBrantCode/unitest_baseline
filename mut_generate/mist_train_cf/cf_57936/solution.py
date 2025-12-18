"""
QUESTION:
Write a function `get_smallest_string` that retrieves the shortest alphanumeric string from an array of mixed type elements, ignoring special characters, null, and non-string values. If the array does not contain any alphanumeric strings, return None.
"""

def get_smallest_string(array):
    alphanumeric_strings = []
    for element in array:
        if element is None or not isinstance(element, str):
            continue
        alphanumeric_string = ''.join(ch for ch in element if ch.isalnum())
        if alphanumeric_string:
            alphanumeric_strings.append(alphanumeric_string)
    return min(alphanumeric_strings, key=len) if alphanumeric_strings else None