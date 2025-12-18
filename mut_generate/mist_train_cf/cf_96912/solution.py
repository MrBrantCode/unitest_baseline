"""
QUESTION:
Search for an element in a list of strings and return its position. The function `search_element` should take two parameters: `list_a` (a list of up to 1000 strings, each with a maximum length of 50 characters) and `element` (the specific string to search for). Return the 0-indexed position of the element if found, and -1 if not found. The solution should have a time complexity of O(n), where n is the number of elements in the list, and should not use any built-in search functions or libraries.
"""

def search_element(list_a, element):
    for i in range(len(list_a)):
        if list_a[i] == element:
            return i
    return -1