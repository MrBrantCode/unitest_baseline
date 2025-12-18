"""
QUESTION:
Create a function named `purge_unusual_symbols` that takes a string of alphanumeric characters as input and returns a string with all non-alphanumeric characters removed.
"""

def purge_unusual_symbols(series):
    return ''.join(ch for ch in series if ch.isalnum())