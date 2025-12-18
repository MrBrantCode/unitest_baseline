"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input, which can contain strings, integers, and nested lists. The function should return a list of unique strings, ignoring case sensitivity, with the following conditions: 

- The function should only consider strings that are at least 5 characters long after removing any leading or trailing whitespaces.
- It should handle cases where the input list contains both strings and integers, as well as nested lists of strings and integers.
- The function should not use any built-in functions or methods for removing duplicates.
- The output list should be sorted in descending order based on the length of each string.
- The function should handle edge cases where the input list is empty or all strings in the list are duplicates.
- The time complexity of the function should be O(n), where n is the length of the input list, and it should use only a constant amount of additional space.
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