"""
QUESTION:
Write a function to remove all empty elements from a given list of strings. The function should take a list of strings as input and return a new list containing only the non-empty strings.
"""

def remove_empty_elements(arr):
    return [x for x in arr if x != ""]