"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of strings as input and returns a list containing only non-duplicate strings. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list. The function should handle uppercase and lowercase letters as distinct characters, remove any leading or trailing whitespace from the strings, and maintain the order of appearance of the non-duplicate strings in the input list.
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