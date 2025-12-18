"""
QUESTION:
Write a function called `remove_duplicates` that takes a list as input, which may contain strings, integers, and nested lists. The function should ignore case sensitivity, remove leading/trailing whitespaces, and only consider strings that are at least 5 characters long. The function should return a list of unique strings in descending order based on their lengths, without using built-in functions or methods for removing duplicates, and with a time complexity of O(n) where n is the length of the input list.
"""

def remove_duplicates(strings):
    unique_strings = set()
    for item in strings:
        if isinstance(item, str):
            item = str(item).strip()
            if len(item) >= 5:
                unique_strings.add(item.lower())
        elif isinstance(item, list):
            unique_strings.update(remove_duplicates(item))
    return sorted(list(unique_strings), key=lambda x: len(x), reverse=True)