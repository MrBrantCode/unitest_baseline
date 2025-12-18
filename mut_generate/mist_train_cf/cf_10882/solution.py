"""
QUESTION:
Create a function called `sort_strings` that sorts a list of strings in alphabetical order in descending fashion. The function should take a list of strings as input and return a new list with the strings sorted. The solution should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_strings(strings):
    return sorted(strings, reverse=True)