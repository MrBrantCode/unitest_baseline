"""
QUESTION:
Create a function named `concatenate_strings` that takes a list of strings as input and returns a string with unique characters from the input strings in lexicographic order. The function should be able to handle up to 10^6 strings with up to 10^6 characters each, and should have a time complexity of O(NlogN) and a space complexity of O(N), where N is the total number of characters in all the strings combined. The function should not use any built-in sorting or deduplication functions or libraries.
"""

def concatenate_strings(strings):
    unique_chars = set()

    for string in strings:
        for char in string:
            unique_chars.add(char)

    sorted_chars = []
    for char in unique_chars:
        inserted = False
        for i, sorted_char in enumerate(sorted_chars):
            if char < sorted_char:
                sorted_chars.insert(i, char)
                inserted = True
                break
        if not inserted:
            sorted_chars.append(char)

    return ''.join(sorted_chars)