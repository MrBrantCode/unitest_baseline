"""
QUESTION:
Write a function `is_enclosed_by` that takes two parameters: a string `str` and a substring `substring`. The function should return `True` if the string `str` starts and ends with the substring `substring`, and `False` otherwise. The function should handle overlapping scenarios and assume that the substring is not empty.
"""

def is_enclosed_by(s, substring):
    return s.startswith(substring) and s.endswith(substring)