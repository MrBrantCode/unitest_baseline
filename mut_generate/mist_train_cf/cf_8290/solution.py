"""
QUESTION:
Create a function named `find_strings` that takes a list of strings and a target string as input. Return a list of tuples where each tuple contains a string from the list and a boolean value indicating whether the string contains the target string. If the target string is empty or contains only whitespace characters, or if the list of strings is empty or contains only empty strings or whitespace strings, return an empty list. Ensure that the function handles duplicate strings in the list and only returns one tuple for each unique string. The function should not modify the original list or strings and should have a time complexity of O(n*m) and a space complexity of O(k), where n is the number of strings, m is the average string length, and k is the number of strings containing the target string.
"""

def find_strings(strings, target):
    if not target or target.isspace():
        return []

    results = set()

    for string in strings:
        if string and not string.isspace():
            results.add((string, target in string))

    return list(results)