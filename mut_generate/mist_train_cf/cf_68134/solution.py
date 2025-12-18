"""
QUESTION:
Write a function `capitalize_initial_pair(s)` that takes a string `s` as input, splits it into words, and returns a new string where the first two characters of each word are capitalized.
"""

def capitalize_initial_pair(s):
    words = s.split(" ")
    result = []
    for word in words:
        result.append(word[:2].upper() + word[2:])
    return " ".join(result)