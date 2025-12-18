"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of strings as input. The function should return a list containing only the non-duplicate strings from the input list, maintaining their order of appearance. The function must handle uppercase and lowercase letters as distinct characters and remove any leading or trailing whitespace from the strings. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates(strings):
    seen = set()
    non_duplicates = []
    for string in strings:
        string = string.strip()
        if string.lower() not in seen:
            seen.add(string.lower())
            non_duplicates.append(string)
    return non_duplicates