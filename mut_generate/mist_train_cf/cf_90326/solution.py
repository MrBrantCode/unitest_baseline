"""
QUESTION:
Create a function `find_strings` that takes a list of strings and a target string as inputs and returns a list of tuples. Each tuple consists of a unique string from the list and a boolean value indicating whether the string contains the target string. If the target string is empty or contains only whitespace characters, or if the input list is empty or contains only empty strings or whitespace strings, return an empty list. The function should handle duplicate strings in the input list by returning only one tuple for each unique string. The time complexity should be O(n*m) and the space complexity should be O(k), where n is the number of strings in the list, m is the average length of the strings, and k is the number of strings in the list that contain the target string.
"""

def find_strings(strings, target):
    if not target or target.isspace() or all(s.strip() == '' for s in strings):
        return []

    results = set()

    for string in strings:
        if string and not string.isspace():
            results.add((string, target in string))

    return list(results)