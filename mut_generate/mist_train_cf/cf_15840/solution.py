"""
QUESTION:
Write a function `reverse_alphabetical_sort` that sorts a list of strings in reverse alphabetical order, ignoring case differences while maintaining the original order of strings with the same value after ignoring case.
"""

def reverse_alphabetical_sort(strings):
    return sorted(strings, key=lambda x: x.lower(), reverse=True)