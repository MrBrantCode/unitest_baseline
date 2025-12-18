"""
QUESTION:
Write a function named `duplicate_characters` that takes a string as input, identifies duplicate characters (i.e., characters that appear more than once), and returns a dictionary where keys are the duplicate characters and values are their frequencies. The function should achieve this in O(n) time complexity, where n is the length of the string, and optimize space complexity by avoiding unnecessary data storage.
"""

def duplicate_characters(string):
    duplicated = {}
    for ch in string:
        if ch in duplicated:
            duplicated[ch] += 1
        else:
            duplicated[ch] = 1
    return {k: v for k, v in duplicated.items() if v > 1}