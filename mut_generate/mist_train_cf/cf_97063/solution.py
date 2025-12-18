"""
QUESTION:
Create a function called `find_substring` that takes two parameters: `string` and `substring`. The function should return the index of the first occurrence of the entire word `substring` in `string`, with the search being case-insensitive. If `substring` is not found in `string`, return -1.
"""

def find_substring(string, substring):
    string = string.lower()
    substring = substring.lower()

    words = string.split()

    for i, word in enumerate(words):
        if word == substring:
            return string.find(word)

    return -1